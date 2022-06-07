board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']



letras_erradas = [1,2,3]
x = len(letras_erradas)
print(x)
if x >= 0:
    if x == 0:
        print(board[0])
    elif x == 1:
        print(board[1])
    elif x == 2:
        print(board[2])
    elif x == 3:
        print(board[3])
    elif x == 4:
        print(board[4])
    elif x == 5:
        print(board[5])
    elif x >= 6:
        print(board[6])