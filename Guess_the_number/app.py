from os import abort
from random import randint, randrange

print("Welcome to RECNEPS MINI GUESS GAME")

HINT1 = "I am the first prime number"
HINT2 = "I am usually the first factor of every even number"
HINT3 = "I am a multiple of 3 with the first prime number"
HINT4 = "I am the number of lines needed to draw a 2D square"
HINT5 = "In spanish I am known as cinco"
HINT6 = "I am 6 times more than 1"
HINT7 = "In French I am the same as the shortened month September"
HINT8 = "I look like infinity but that is beyond me"
HINT9 = "I am the product of the multiplication of 3 and itself"
HINT10 = "Diez, diz, that's usally my name"

game_number = randint(0,10)
HINT = [HINT1,HINT2,HINT3,HINT4,HINT5,HINT6,HINT7,HINT8,HINT9,HINT10]
attempt = 3
winner = "You won"
loser = "You lost"

while attempt > 0:
    if game_number == 1:
        print(HINT1)
    elif game_number == 2:
        print(HINT2)
    elif game_number == 3:
        print(HINT3)
    elif game_number == 4:
        print(HINT4)
    elif game_number == 5:
        print(HINT5)
    elif game_number == 6:
        print(HINT6)
    elif game_number == 7:
        print(HINT7)
    elif game_number == 8:
        print(HINT8)
    elif game_number == 9:
        print(HINT9)
    else:
        print(HINT10)

    guess = int(input('Enter a number: \n'))

    if guess == game_number:
        print(winner)
        break
    else:
        print(loser)
        attempt -= 1
        continue

