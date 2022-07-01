from random import randint

print("Welcome to RECNEPS MINI GUESS GAME")

hint_higher = "The number is higher than this"
hint_lower = "The number is lower than this"
final_hint_higher = "The number is higher than this"
final_hint_lower =  "The number is lower than this"
game_number = randint(0,10)
winner = "You won"
loser = "Sorry, Try again"

def game():
    attempt = 3
    while attempt > 0:
        try:
            guess = int(input('Enter a number: \n'))
            if guess == game_number:
                print(winner)
                break
            elif guess > game_number:
                if attempt == 2:
                    print(f"Last try and {final_hint_lower}")
                    attempt -= 1
                else:
                    print(hint_lower)
                    attempt -= 1
                    continue
            elif guess < game_number:
                if attempt == 2:
                    print(f"Last try and {final_hint_higher}")
                    attempt -= 1
                else:
                    print(hint_higher)
                    attempt -= 1
                    continue
        except ValueError:
            print("Sorry, this game accepts integers only")
    
    if guess == game_number:
        print("Congratulations you beat the game")
    else:
        print("Sorry, you've run out of guesses")
    print(f"Also the right answer was {game_number}")

def main():
    game()

if __name__ == '__main__':
    main()
