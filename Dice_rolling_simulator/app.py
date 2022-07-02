from random import randint

def welcome():
    game_yes = ["Yes", "yes"]
    game_no = ["No", "no"]
    print("Welcome to the Dice Rolling Simulator")
    proceed = str(input("To play, please enter Yes or No to quit.\n"))
    if proceed in game_yes:
        dice_rolling_game()
    elif proceed in game_no:
        quit_game()
    else:
        print("Please enter Yes or No")
        welcome()

    while True:
        play_again = input("To play again, please enter Yes or No to quit\n")
        if play_again in game_yes:
            dice_rolling_game()
            continue
        else:
            quit_game()
            break
        
def quit_game():
    print("Sad to see you go!")

def dice_rolling_game():
    die = randint(1,6)
    print(f"The die came up {die}")

def main():
    welcome()

if __name__ == "__main__":
    main()