import random
from words import words

yes = ["Yes","yes", "Y", "y"]
no = ["No", "no", "N", "n"]
def welcome():
    print("Welcome to the Hangman Game")
    play_option = input("To play, please enter yes or enter no to quit.\n")
    if play_option in yes:
        hangman()
    

def hangman():
    random_word = random.choice(words).upper()
    word_to_guess = "_" * len(random_word)
    print(word_to_guess)

def main():
    welcome()

if __name__ == "__main__":
    main()