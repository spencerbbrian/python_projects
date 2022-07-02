from random import randint

def welcome():
    game_yes = ["Yes", "yes"]
    game_no = ["No", "no"]
    print("Welcome to the Dice Rolling Simulator")
    proceed = str(input("To play, please enter Yes or enter No to quit.\n"))
    if proceed in game_yes:
        game_type = int(input("How many dice do you want to roll? \n"))
        if game_type == 1:
            die_rolling_game()
            while True:
                play_again = input("To play again, please enter Yes or enter No to quit\n")
                if play_again in game_yes:
                    die_rolling_game()
                    continue
                else:
                    welcome()
                    break
        if game_type == 2:
            two_dice_game()
            while True:
                play_again = input("To play again, please enter Yes or No to quit\n")
                if play_again in game_yes:
                    two_dice_game()
                    continue
                else:
                    welcome()
                    break
    elif proceed in game_no:
        quit_game()
    else:
        print("Please enter Yes or No")
        welcome()

def two_dice_game():
    die1 = randint(1,6)
    die2 = randint(1,6)

    total_dice = die1 + die2
    print(f"The dice came up as {total_dice}")

        
def quit_game():
    print("Sad to see you go!")

def die_rolling_game():
    die = randint(1,6)
    print(f"The die came up {die}")

def main():
    welcome()

if __name__ == "__main__":
    main()