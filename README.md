# self.py - Hangman game
https://campus.gov.il/course/course-v1-cs-gov_cs_selfpy101/

* [Game code](https://github.com/boaz209/self.py-course-/blob/master/Tree_man_game.py)
* [Exercise code] (https://github.com/boaz209/self.py-course-/blob/master/Self_py.py)

### פלט הצלחה לדוגמה

```

  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/

Enter file path: Python-Tree-Man-master\Main project\word.txt
Enter index: 1
Let’s start!

x-------x

Guess a letter: ^
X
:(
_ _ _
Guess a letter: T
_ _ t 
Guess a letter: b
:(
_ _ t

x-------x
|
|
|
|
|

Guess a letter: c
c _ t 
Guess a letter: t
X WORNG X
b -> c -> t
c _ t
Guess a letter: p
:(
c _ t

x-------x
|       |
|       0
|
|
|

Guess a letter: a
c a t
---------------WIN---------------

```





### פלט כישלון לדוגמה

```

  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/

Enter file path: Python-Tree-Man-master\Main project\word.txt
Enter index: 1
Let’s start!

x-------x

Guess a letter: ^
X
:(
_ _ _
Guess a letter: T
_ _ t 
Guess a letter: b
:(
_ _ t

x-------x
|
|
|
|
|

Guess a letter: c
c _ t 
Guess a letter: t
X WORNG X
b -> c -> t
c _ t
Guess a letter: p
:(
c _ t

x-------x
|       |
|       0
|
|
|

Guess a letter: s
:(
c _ t

x-------x
|       |
|       0
|       |
|
|

Guess a letter: &3
X
:(
c _ t
Guess a letter: M
:(
c _ t

x-------x
|       |
|       0
|      /|\
|
|

Guess a letter: o
:(
c _ t

x-------x
|       |
|       0
|      /|\
|      /
|

Guess a letter: f
:(
c _ t

x-------x
|       |
|       0
|      /|\
|      / \
|

---------------LOSE---------------
```
