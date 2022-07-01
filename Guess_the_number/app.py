from random import randint

def welcome(): 
    print("Welcome to RECNEPS MINI GUESS GAME\n")
    print("Easy - 1")
    print("Intermediate - 2")
    print("Hard - 3")

    difficulty = int(input("Please enter a difficulty from 1 to 3: \n"))
    if difficulty == 1:
        easy()
    elif difficulty == 2:
        Intermediate()
    elif difficulty == 3:
        Hard()
    else:
        print("Wrong input")
        welcome()



hint_higher = "The number is higher than this"
hint_lower = "The number is lower than this"
final_hint_higher = "The number is higher than this"
final_hint_lower =  "The number is lower than this"
easy_game_number = randint(0,10)
intermediate_game_number = randint(0,100)
hard_game_number = randint(0,1000)
winner = "You won"
loser = "Sorry, Try again"

def easy():
    attempt = 3
    while attempt > 0:
        try:
            guess = int(input('Enter a number from 0 to 10: \n'))
            if guess == easy_game_number:
                print(winner)
                break
            elif guess > easy_game_number:
                if attempt == 2:
                    print(f"Last try and {final_hint_lower}")
                    attempt -= 1
                else:
                    print(hint_lower)
                    attempt -= 1
                    continue
            elif guess < easy_game_number:
                if attempt == 2:
                    print(f"Last try and {final_hint_higher}")
                    attempt -= 1
                else:
                    print(hint_higher)
                    attempt -= 1
                    continue
        except ValueError:
            print("Sorry, this game accepts integers only")
    
    if guess == easy_game_number:
        print("Congratulations you beat the game")
    else:
        print("Sorry, you've run out of guesses")
        print(f"Also the right answer was {easy_game_number}")

def Intermediate():
    attempt = 5
    while attempt > 0:
        try:
            guess = int(input('Enter a number from 0 to 100: \n'))
            if guess == intermediate_game_number:
                print(winner)
                break
            elif guess > intermediate_game_number:
                if attempt == 2:
                    print(f"Last try and {final_hint_lower}")
                    attempt -= 1
                else:
                    print(hint_lower)
                    attempt -= 1
                    continue
            elif guess < intermediate_game_number:
                if attempt == 2:
                    print(f"Last try and {final_hint_higher}")
                    attempt -= 1
                else:
                    print(hint_higher)
                    attempt -= 1
                    continue
        except ValueError:
            print("Sorry, this game accepts integers only")
    if guess == intermediate_game_number:
        print("Congratulations you beat the game")
    else:
        print("Sorry, you've run out of guesses")
        print(f"Also the right answer was {intermediate_game_number}")

def Hard():
    attempt = 10
    while attempt > 0:
        try:
            guess = int(input('Enter a number from 0 to 1000: \n'))
            if guess == hard_game_number:
                print(winner)
                break
            elif guess > hard_game_number:
                if attempt == 2:
                    print(f"Last try and {final_hint_lower}")
                    attempt -= 1
                else:
                    print(hint_lower)
                    attempt -= 1
                    continue
            elif guess < hard_game_number:
                if attempt == 2:
                    print(f"Last try and {final_hint_higher}")
                    attempt -= 1
                else:
                    print(hint_higher)
                    attempt -= 1
                    continue
        except ValueError:
            print("Sorry, this game accepts integers only")
    
    if guess == hard_game_number:
        print("Congratulations you beat the game")
    else:
        print("Sorry, you've run out of guesses")
        print(f"Also the right answer was {hard_game_number}")

def main():
    welcome()

if __name__ == '__main__':
    main()
