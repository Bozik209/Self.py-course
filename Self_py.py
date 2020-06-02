# Self.py חורף
import calendar
from collections import Counter
import filecmp
import getpass

# רמת קושי: בינוני תרגיל 9.3.2
def my_mp4_playlist(file_path, new_song):
    with open(file_path) as f:
        count = sum(1 for _ in f)

    # check if in the file have 3 lines if not is add new lines
    while count<=3:
        r = open(file_path, "a")
        r.write("new line\n")
        count+=1
        r.close()

    if count>=3:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        # now we have an array of lines. If we want to edit the line 3...
        if len(lines) > int(3):
            clear_line=lines[2].split(";")
            clear_line[0]=new_song
            temp_new_song =';'.join(clear_line)
            lines[2] = temp_new_song

        with open(file_path, 'w') as file:
            file.writelines(lines)

        get_mp4_playlist = open(file_path, "r")
        print(get_mp4_playlist.read())



my_mp4_playlist(r"C:\\Users\\boaz\\Desktop\\hi\\songs.txt","Python Love Story")


input()
print("--------------------------------------------")

# רמת קושי: בינוני תרגיל 9.3.1
def my_mp3_playlist(file_path):
    longest_song=0.0
    longest_song_name=""
    most_show_performer=""
    count_show_performer=0

    # Longest song
    get_mp3_playlist=open(file_path, 'r')
    for key in get_mp3_playlist:
        if float(key.split(";")[2].replace(":",".")) >longest_song:
            longest_song=float(key.split(";")[2].replace(":","."))
            longest_song_name=key.split(";")[0]
    print(longest_song_name, longest_song)


    # number of song
    count_of_song = len(open(file_path).readlines())
    print(count_of_song)

    # most view performer
    data = open(file_path).read()
    get_mp3_playlist=open(file_path, 'r')
    for key in get_mp3_playlist:
        count = data.count(key.split(";")[1])
        if count> count_show_performer:
            most_show_performer=key.split(";")[1]
    print(most_show_performer)

    playlist=(longest_song_name,count_of_song,most_show_performer)
    return playlist


print(my_mp3_playlist(r"C:\\Users\\boaz\\Desktop\\hi\\songs.txt"))
# ('Tudo Bom', 5, 'The Black Eyed Peas')

'''
הפונקציה מחזירה טאפל שבו:
    האיבר הראשון הוא מחרוזת המייצגת את שם השיר הארוך ביותר בקובץ (הכוונה היא לשיר הארוך ביותר, הניחו שכל האורכים שונים).
    האיבר השני הוא מספר המייצג את מספר השירים שהקובץ מכיל.
    האיבר השלישי הוא מחרוזת המייצגת את שם המבצע שמופיע בקובץ מספר הפעמים הגדול ביותר (הניחו שיש רק אחד כזה).
    
'''

input()
print("--------------------------------------------")
# רמת קושי: בינוני תרגיל 9.2.3
def who_is_missing(file_name):
    get_number=open(file_name,'r').read()
    number_list=[]

    # sort the text inside the file
    for word in get_number:
        if word != ',':
            number_list.append(word)
    number_list.sort()

    # find the missing number
    for i in range(len(number_list)):
        if i+1 < len(number_list):
            if int(number_list[i])+1 != int(number_list[i+1]):
                found = int(number_list[i])+1
                print("found: ",found)
                # write new file
                found_number = open("C:\\Users\\boaz\\Desktop\\hi\\found.txt", "w")
                found_number.write(str(found))
                found_number.close()




who_is_missing("C:\\Users\\boaz\\Desktop\\hi\\findMe.txt")

'''
קובץ שנקרא findMe.txt:
8,1,9,7,4,6,3,2

הרצת הפונקציה who_is_missing על הקובץ findMe.txt:
>>> who_is_missing("c:\findMe.txt")
5

לאחר ההרצה לעיל של הפונקציה who_is_missing נוצר קובץ חדש שנקרא found.txt:
5
'''

input()
print("--------------------------------------------")
# רמת קושי: קל תרגיל 9.2.2
def copy_file_content(source, destination):
    print(open(source).read())
    dest_w=open(destination,"w")
    dest_w.write(open(source).read())
    dest_w.close()
    print(open(destination).read())



copy_file_content("C:\\Users\\boaz\\Desktop\\hi\\copy.txt", r"C:\Users\boaz\Desktop\hi\paste.txt")
'''
קובץ שנקרא copy.txt:
Copy this text to another file.

קובץ שנקרא paste.txt:
-- some random text --

הרצת הפונקציה copy_file_content עם הקבצים copy.txt ו-paste.txt:
>>> copy_file_content("copy.txt", "paste.txt")

הקובץ paste.txt לאחר ההרצה לעיל של הפונקציה copy_file_content:
Copy this text to another file.
'''

input()
print("--------------------------------------------")


# רמת קושי: בינוני תרגיל 9.1.2
def sort_file(file):
    list_file=[]
    # get word from file
    for line in file:
        for word in line.split():
            if word not in list_file:
                list_file.append(word)

    list_file.sort()
    print(list_file)
    file.close()

def rev_file(file):
    for line in file:
        print(line[::-1])
    file.close()

def last_file(file,line_number):
    lines = file.readlines()
    print(lines[-line_number:])


files_path=open(r"C:\Users\boaz\Desktop\hi\sampleFile.txt")
#input("Enter a file path: ")
task=input("Enter a task: sort/ rev/ last :")

if task == "sort":
    sort_file(files_path)
    # ['about', 'and', 'away', 'believe', 'can', 'day', 'every', 'fly', 'i', 'it', 'my', 'night', 'sky', 'spread', 'the', 'think', 'touch', 'wings']

if task == "rev":
    rev_file(files_path)
    #yks eht hcuot nac i eveileb i ylf nac i eveileb i
    #yawa ylf dna sgniw ym daerps yad dna thgin yreve ti tuoba kniht i

if task == "last":
    line_number=int(input("Enter a number: "))
    last_file(files_path,line_number)
    # i think about it every night and day spread my wings and fly away

'''
text file: 
i believe i can fly i believe i can touch the sky
i think about it every night and day spread my wings and fly away
'''

input()
print("--------------------------------------------")

# רמת קושי: קל תרגיל 9.1.1
def are_files_equal(file1, file2):
    a_file = open(file1, 'r')
    print(a_file.read())

    b_file = open(file2, 'r')
    print(b_file.read())

    print(filecmp.cmp(file1,file2))

are_files_equal(r"C:\Users\boaz\Desktop\hi\vacation.txt", r"C:\Users\boaz\Desktop\hi\work.txt")

# name =getpass.getuser()
# are_files_equal(r"C:\Users\{}\Desktop\hi\vacation.txt", r"C:\Users\boaz\Desktop\hi\work.txt".format(name))

input()
print("--------------------------------------------")

# רמת קושי: קל תרגיל 8.3.4
def inverse_dict(my_dict):
    new_dict={}
    for i in my_dict:
        if my_dict[i] in new_dict:
            new_dict[my_dict[i]].append(i)
        else:
            new_dict.update({my_dict[i]:[i]})
    print(new_dict)






course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
inverse_dict(course_dict)
# {3: ['I', 'love'], 2: ['self.py!']}

input()
print("--------------------------------------------")
# רמת קושי: קל תרגיל 8.3.3
def count_chars(my_str):
    count_dict={}
    for i in my_str:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    print(count_dict)

    # with build func
    print(Counter(my_str))

magic_str = "abra cadabra"
count_chars(magic_str)
#{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}


input()
print("--------------------------------------------")

# רמת קושי: קל תרגיל 8.3.2
new_dict ={"first_name":"Mariah","last_name":"Carey","birth_date":"27.03.1970","hobbies":["Sing", "Compose", "Act"]}

Choose=int(input("Choose 1-7: "))

if Choose == 1:
    print(new_dict["last_name"])
if Choose == 2:
    print(new_dict["birth_date"])
if Choose == 3:
    print(new_dict["hobbies"])
if Choose == 4:
    print(new_dict["hobbies"][-1])
if Choose == 5:
    new_dict["hobbies"].append("Cooking")
    print(new_dict["hobbies"])
if Choose == 6:
    new_dict["birth_date"]=("27","03","1970")
    print(new_dict["birth_date"])
if Choose == 7:
    new_dict["age"]=2020-int(new_dict["birth_date"][6:])
    print(new_dict["age"])

input()
print("--------------------------------------------")

# רמת קושי: אתגר תרגיל 8.2.4
def sort_anagrams(list_of_strings):
    resList=[]
    tempList=[]
    for i in range(len(list_of_strings)):
        for y in range(len(list_of_strings)):
            if set(filter(str.isalnum, list_of_strings[i])) == set(filter(str.isalnum, list_of_strings[y])):
                if list_of_strings[y] not in tempList:
                    tempList.append(list_of_strings[y])
    resList.append(tempList)
    print(resList)

list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
sort_anagrams(list_of_words)

print("--------------------------------------------")

# רמת קושי: קשה תרגיל 8.2.3
def mult_tuple(tuple1, tuple2):
    tuple3=()
    tuple4=()
    for i in tuple1:
        for y in tuple2:
            tuple3 = i,   y
            tuple4+= (tuple3,tuple3[::-1])
    print(tuple4)

first_tuple = (1, 2)
second_tuple = (4, 5)
mult_tuple(first_tuple, second_tuple)
# ((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2))
# ((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2))

first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
mult_tuple(first_tuple, second_tuple)
#((1, 4), (4, 1), (1, 5), (5, 1), (1, 6), (6, 1), (2, 4), (4, 2), (2, 5), (5, 2), (2, 6), (6, 2), (3, 4), (4, 3), (3, 5), (5, 3), (3, 6), (6, 3))
#((1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 1), (5, 1), (6, 1), (4, 2), (5, 2), (6, 2), (4, 3), (5, 3), (6, 3))

print("--------------------------------------------")
# רמת קושי: בינוני תרגיל 8.2.2
def sort_prices(list_of_tuples):
    print(sorted(list_of_tuples, key=lambda x: x[1] ,reverse=True))

products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
sort_prices(products)

print("--------------------------------------------")

# רמת קושי: קל תרגיל 8.2.1
data = ("self", "py", 1.543)
format_string = "Hello"

print("Hello %s. %s learner, you have only %.1f units left before you master the course!" % data)


print("--------------------------------------------")
# רמת קושי: אתגר תרגיל 7.2.7
def arrow(my_char, max_length):
    for x in range(max_length):
        for y in range(x+1):
            print(my_char, end =" ")
        print()

    for y in range(max_length):
        for x in range(x):
            print(my_char, end =" ")
        print()

arrow('*', 5)

print("--------------------------------------------")
# רמת קושי: בינוני תרגיל 7.2.6


print("--------------------------------------------")

#רמת קושי: בינוני תרגיל 7.2.5
def sequence_del(my_str):
    l = []
    last = ''
    for ch in my_str:
        if last != ch:
            l.append(ch)
            last = ch
    print("".join(l))


sequence_del("ppyyyyythhhhhooonnnnn")
# 'python'
sequence_del("SSSSsssshhhh")
# 'Ssh'
sequence_del("Heeyyy   yyouuuu!!!")
# 'Hey you!'
print("--------------------------------------------")

# רמת קושי: קל תרגיל 7.2.3
def seven_boom(end_number):
    sevenList=[]
    for boom in range(end_number+1):
        if boom == 7 or boom % 7 == 0 or '7' in str(boom):
            sevenList.append('BOOM')
        else:
            sevenList.append(boom)
    return sevenList

print(seven_boom(17))
#['BOOM', 1, 2, 3, 4, 5, 6, 'BOOM', 8, 9, 10, 11, 12, 13, 'BOOM', 15, 16, 'BOOM']

print("--------------------------------------------")

# רמת קושי: קל תרגיל 7.2.2
def numbers_letters_count(my_str):
    letters_count=0
    num_count=0
    for letters in my_str:
        if letters.isdigit():
            num_count += 1
        else:
            letters_count += 1
    return [num_count,letters_count]


print(numbers_letters_count("Python 3.6.3"))
#[3, 9]

print("--------------------------------------------")

# רמת קושי: קל תרגיל 7.2.1
def is_greater(my_list, n):
    result=[]
    for num in my_list:
        if num > n:
            result.append(num)
    return result

result = is_greater([1, 30, 25, 60, 27, 28], 28)
print(result)
#[30, 60]

print("--------------------------------------------")

# רמת קושי: קל תרגיל 7.1.4
def squared_numbers(start, stop):
    Liststart=[]
    while start <= stop:
        Liststart.append(start * start)
        start = start + 1
    print(Liststart)

squared_numbers(4, 8)
#[16, 25, 36, 49, 64]
squared_numbers(-3, 3)
#[9, 4, 1, 0, 1, 4, 9]

print("--------------------------------------------")

#רמת קושי: קל תרגיל 6.3.2
def longest(my_list):
    print(max(my_list,key=len))



list1 = ["111", "234", "2000", "goru", "birthday", "09"]
longest(list1)

print("--------------------------------------------")

# רמת קושי: קל תרגיל 6.3.1
def are_lists_equal(list1, list2):
    if sorted(list1) == sorted(list2):
        print(True)
    else:
        print(False)

list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]

are_lists_equal(list1, list2)
are_lists_equal(list1, list3)
print("--------------------------------------------")

# רמת קושי: אתגר תרגיל 6.2.4
def extend_list_x(list_x, list_y ):
        temp=list_x
        list_x=len(list_y)+len(list_x)
        list_x=list_y
        list_x.append(temp)
        print(list_x)

x = [4, 5, 6]
y = [1, 2, 3]
extend_list_x(x, y)

# [1, 2, 3, 4, 5, 6]
print("--------------------------------------------")

# רמת קושי: בינוני תרגיל 6.2.3
def format_list(my_list):
    new_list=my_list[::2]+ ["and"] +my_list[-1:]
    print(', '.join(new_list))

my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
format_list(my_list)

print("--------------------------------------------")

# רמת קושי: קל תרגיל 6.1.2
def shift_left(my_list):
    a,b,c =my_list
    my_list=b,c,a
    print(my_list)



shift_left([0, 1, 2])
shift_left(['monkey', 2.0, 1])
# >>> shift_left([0, 1, 2])
# [1, 2, 0]
# >>> shift_left(['monkey', 2.0, 1])
# [2.0, 1, 'monkey']



print("--------------------------------------------")

# רמת קושי: קל תרגיל 5.4.1
def func(num1, num2):
    pass
    #<return a value>


print("--------------------------------------------")

# רמת קושי: אתגר  תרגיל 5.3.7
def chocolate_maker(small, big, x):
    # options 1
    # if (small*1 + big * 5) >= x:
    #     print(True)
    # else:
    #     print(False)

    # options 2
    print(True) if (small * 1 + big * 5) >= x else print(False)


chocolate_maker(3, 1, 8)
chocolate_maker(3, 1, 9)
chocolate_maker(3, 2, 10)

print("--------------------------------------------")

# רמת קושי: בינוני תרגיל 5.3.6
def fix_age(age):
    if age >= 13 and age <= 19 and age != 15 and age != 16:
        age=0
        return age
    return age


def filter_teens(a=13, b=13, c=13):
    a=fix_age(a)
    b=fix_age(b)
    c=fix_age(c)
    print(a+b+c)


filter_teens()
filter_teens(1, 2, 3)
filter_teens(2, 13, 1)
filter_teens(2, 1, 15)

print("--------------------------------------------")
# תרגיל 5.3.5
def distance(num1, num2, num3):
    if abs(num3-num1) == 1 or abs(num2-num1) == 1:
        if abs(num2-num1) > 2 or abs(num2-num3) > 2:
            return True
        if abs(num3-num1) > 2 or abs(num3-num2) > 2:
            return True
    return False

print(distance(1, 2, 10))
print(distance(4, 5, 3))

print("--------------------------------------------")

# תרגיל 5.3.4
def last_early(my_str):
    print(bool(my_str.find(my_str[-1:])) if my_str.find(my_str[-1:])+1 != len(my_str) else False)


last_early("happy birthday")
last_early("best of luck")
last_early("Wow")
last_early("X")
print("--------------------------------------------")

# תרגיל 4.2.4

date=input("Enter a date (dd/mm/yyyy) : ")  #01/01/2000
new_date=date.split('/')
print(list(calendar.day_name)[calendar.weekday(int(new_date[2]),int(new_date[1]),int(new_date[0]))])
print("--------------------------------------------")


# תרגיל 4.2.3
temperature = input("Insert the temperature you would like to convert: ")
dgree=temperature[-1:]
number=float(temperature[0:-1])

if temperature[-1::] == 'F' or temperature[-1::] == 'f':
    convert_temp=(5*number-160)/9
    print(convert_temp,'C')


if temperature[-1::] == 'C' or temperature[-1::] == 'c':
    convert_temp = (9 * number + (32*5)) / 5
    print(convert_temp,'F')
print("--------------------------------------------")


# תרגיל 4.2.2

palindrome = input("Enter a word: ")
if palindrome[::-1] == palindrome:
    print("OK")
else:
    print("NOT")
print("--------------------------------------------")


# תרגיל 3.4.3

Test_343="astronaut"
print(Test_343[0:len(Test_343)//2] + Test_343[len(Test_343)//2:].upper())

print("--------------------------------------------")


# תרגיל 3.4.2
ddar=input("Please enter a string: ")
#x="ddar astronaut. pldase, stop drasing md!"
new_ddar=ddar[0] + ddar[1::].replace("d","e")
print(new_ddar)
#dear astronaut. please, stop erasing me!
print("--------------------------------------------")




# תרגיל 3.3.3
encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"

print(encrypted_message[:2:-1].replace('X', ''))
print("--------------------------------------------")




# תרגיל 3.2.1
text_taki = """"Shuffle, Shuffle, Shuffle", say it together! 
Change colors and directions, 
Don't back down and stop the player! 
\t Do you want to play Taki? \n  \
\t Press y\\n """

print(text_taki)
print("--------------------------------------------")





# תרגיל 2.3.3
bricks = int(input("Enter three digits (each digit for one pig): "))
total_bricks=(bricks//100)+((bricks%100)//10)+((bricks%100)%10)

print("Total bricks : " , total_bricks)
print("bricks for each one : ", total_bricks//3)
print("bricks left each one : ", total_bricks%3)
print((total_bricks % 3 == False))
print("--------------------------------------------")


'''
כתבו תוכנית שמקבלת מהמשתמש תאריך במבנה dd/mm/yyyy ומדפיסה את היום בשבוע עבור התאריך שהוזן.
'''
import calendar

date=input("Enter a date (dd/mm/yyyy) : ")  #01/01/2000
new_date=date.split('/')
print(list(calendar.day_name)[calendar.weekday(int(new_date[2]),int(new_date[1]),int(new_date[0]))])



'''
תבו תוכנית שממירה בין טמפרטורה במעלות צלזיוס לטמפרטורה במעלות פרנהייט.
התוכנית קולטת מהמשתמש טמפרטורה: או במעלות צלזיוס, עם סיומת C, או במעלות פרנהייט, עם סיומת F.
אם הטמפרטורה במעלות צלזיוס, תמיר אותה למעלות פרנהייט, ואם הטמפרטורה במעלות פרנהייט, תמיר אותה למעלות צלזיוס.
'''
print("--------------------------------------------")
temperature = input("Insert the temperature you would like to convert: ")
dgree=temperature[-1:]
number=float(temperature[0:-1])

if temperature[-1::] == 'F' or temperature[-1::] == 'f':
    convert_temp=(5*number-160)/9
    print(convert_temp,'C')


if temperature[-1::] == 'C' or temperature[-1::] == 'c':
    convert_temp = (9 * number + (32*5)) / 5
    print(convert_temp,'F')


'''
כתבו תוכנית שקולטת מהמשתמש מחרוזת לבחירתו.
התוכנית תדפיס למסך מחרוזת בה כל המופעים של התו הראשון הוחלפו בתו 'e', למעט התו הראשון עצמו.

דוגמה להרצת התוכנית

Please enter a string: ddar astronaut. pldase, stop drasing md!
dear astronaut. please, stop erasing me!
'''
print("--------------------------------------------")
x=input("Please enter a string: ")
#x="ddar astronaut. pldase, stop drasing md!"
new_x=x[0] + x[1::].replace("d","e")
print(new_x)
#dear astronaut. please, stop erasing me!



'''
כתבו תוכנית שקולטת מהמשתמש מחרוזת לבחירתו.
התוכנית מדפיסה את המחרוזת כאשר האותיות בחצי הראשון של המחרוזת הן אותיות קטנות, והאותיות בחצי השני של המחרוזת הן אותיות גדולות.
אם אורך המחרוזת אי זוגי, החצי הראשון יהיה קטן באחת מהחצי השני.
'''
print("--------------------------------------------")
y=input("Please enter a string: ") #astronaut
new_y=y[:len(y)//2]+y[len(y)//2:].upper()
print(new_y)  #astrONAUT




'''
כתבו תוכנית שקולטת מהמשתמש מחרוזת ומדפיסה 'OK' אם היא פלינדרום, אחרת 'NOT'.
'''
print("--------------------------------------------")
palindrome = input("Enter a word: ")
if palindrome[::-1] == palindrome:
    print("OK")
else:
    print("NOT")


