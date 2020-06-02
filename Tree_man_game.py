import random
import sys
import os


def Print_Hangman(number):
    if number == 7:
        print(
            """
x-------x
            """
        )

    if number == 6:
        print(
            """
x-------x
|
|
|
|
|
            """
        )

    if number == 5:
        print(
            """
x-------x
|       |
|       0
|
|
|
            """
        )

    if number == 4:
        print(
            """
x-------x
|       |
|       0
|       |
|
|
            """
        )

    if number == 3:
        print(
            """
x-------x
|       |
|       0
|      /|\\
|
|
            """
        )

    if number == 2:
        print(
            """
x-------x
|       |
|       0
|      /|\\
|      /
|
                """
        )

    if number == 1:
        print(
            """
x-------x
|       |
|       0
|      /|\\
|      / \\
|
                """
        )


print(
    """
  _    _                                       
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
"""
)

# ------------------------------ Func ---------------------------
def valid_letter(letter_guess):
    if not letter_guess.isalpha() and len(letter_guess) > 1:
        return False
    elif not letter_guess.isalpha():
        return False
    elif len(letter_guess) > 1:
        return False
    return True


# רמת קושי: בינוני תרגיל 6.4.2
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if letter_guessed in old_letters_guessed:
        print("X WORNG X")
        old_letters_guessed.sort()
        print(" -> ".join(old_letters_guessed))
        return False        
    old_letters_guessed.append(letter_guessed)
    return True


# רמת קושי: בינוני תרגיל 7.3.1
def show_hidden_word(secret_word, old_letters_guessed, word,letter_guess,MAX_TRIES):
    bool_check =False
    for i in range(len(word)):
        if letter_guess not in word:
            print(":(")  
            bool_check = True
            break

    # do the same like the func just in for loop
    # check_valid_input(letter_guessed, old_letters_guessed) 
    for i in range(len(word)):
        if word[i] in old_letters_guessed:
            secret_word = secret_word[:i] + word[i] + secret_word[i + 1 :]
    print(secret_word)
    return bool_check




# רמת קושי: בינוני תרגיל 7.3.2
def check_win(word, old_letters_guessed):
    for letter in word:
        if letter not in old_letters_guessed:
            return False
    return True



# רמת קושי: בינוני תרגיל 9.4.1
def choose_word(file_path, index):
    file = open(file_path, "r")
    word_from_txt = ()
    word = file.read()

    # if index is less text count word
    if index < word.count(" "):
        file = open(file_path, "r")
        for i in file.readlines():
            word_from_txt = (i.split(" ")[index - 1],)

    # if index is more text count word, so is loop the text
    if index > word.count(" "):
        i = 0
        temp_index = index
        while temp_index != 0:
            i += 1
            temp_index -= 1
            if i > word.count(" "):
                i = 0
        word_from_txt = (word.split(" ")[i],)
    file.close()

    # find the count of word that show once
    file_Wcnt = open(file_path, "r")
    cnt = 0

    for w in file_Wcnt.readlines():
        for ww in w.split(" "):
            if w.split(" ").count(ww) <= 1:
                cnt += 1
    file_Wcnt.close()



    file_Wcnt = open(file_path, "r")
    word_from_txt = (
        word_from_txt[:0] + (file_Wcnt.read().count(" ") - cnt,) + word_from_txt[0:]
    )
    return str(word_from_txt[1])


# ------------------------------ Main ---------------------------
old_letters_guessed = []


def main():

    path_file=input("Enter file path: ")
    index_file=int(input("Enter index: "))

    # רמת קושי: בינוני תרגיל 9.4.1
    clean_word=choose_word(path_file, index_file)

    # Get the secret word from user
    secret_word = len(clean_word) * "_ "
    word = "_".join(clean_word)


    print("Let’s start!")
    MAX_TRIES=7
    Print_Hangman(MAX_TRIES)
    MAX_TRIES -=  1    


    while MAX_TRIES > 0:
        letter_guess = input("Guess a letter: ").lower()

        while valid_letter(letter_guess):
            if valid_letter(letter_guess):
                try_update_letter_guessed(letter_guess, old_letters_guessed)
                break
            letter_guess = input("Guess a letter: ").lower()
        else:
            print("X")
     
        # Print if the guess is worng
        if show_hidden_word(secret_word, old_letters_guessed, word,letter_guess,MAX_TRIES) and valid_letter(letter_guess):
            Print_Hangman(MAX_TRIES)
            MAX_TRIES -=  1    
            

        if check_win(clean_word, old_letters_guessed):
            print("---------------WIN---------------")
            sys.exit()
            break
    
    print("---------------LOSE---------------")

if __name__ == "__main__":
    main()

