import random
from words import words

yes = ["Yes","yes", "Y", "y"]
no = ["No", "no", "N", "n"]
def welcome():
    print("Welcome to the Hangman Game")
    play_option = input("To play, please enter yes or enter no to quit.\n")
    if play_option in yes:
        hangman()
    elif play_option in no:
        print("Bye!")
    else:
        print("Wrong input")
        welcome()

def hangman():
    random_word = random.choice(words).upper()
    word_to_guess = "_" * len(random_word)
    random_word_enumerated = list(enumerate(random_word))
    final_random_word = []
    guessed_word = []
    for index_letter in random_word_enumerated:
        final_random_word.append(index_letter[1])
    # print(final_random_word)
    print(word_to_guess)
    attempts = 6
    while attempts > 0:
        gues = input("Please enter a letter.\n")
        guess = gues.upper()
        if guess.isalpha and len(guess) == 1:
                if guess in final_random_word:
                    print(f"Correct. {guess} is in this word")
                    if guess in guessed_word:
                        print("You have already guessed this.")
                    else:
                        guessed_word.append(guess)
                        list_word_to_guess = list(word_to_guess)
                        print(list_word_to_guess)
                        # If the letter in {random_word} == guess, append the letter in indices. This does it at the same place
                        indices = [i for i, letter in enumerate(random_word)
                        if letter == guess]
                        for index in indices:
                            list_word_to_guess[index] = guess
                        word_to_guess = "".join(list_word_to_guess)
                        print(word_to_guess)
                    attempts -= 1
                    if "_" not in word_to_guess:
                        print(f"Congratulations! You won with {attempts} left")
                        play_again()
                    continue
                else:
                    print("Bad try! Try again.")
                    attempts -= 1
                    continue
        else:
            print("Sorry, wrong input.")
            continue
    if attempts < 1 and ("_" in word_to_guess):
        print("You lost!")
        welcome()
    elif attempts < 1 and (len("_" in word_to_guess) == 0):
        print("Wow you somehow won. Congratulations!")

def play_again():
    print("Do you want to play again?\n")
    game_again = input("Enter yes to play again or no to quit.\n")
    if game_again in yes:
        hangman()
    elif game_again in no:
        print("Sad to see you go. Bye!")
        exit()
    else:
        print("Please enter with yes or no.\n")
        play_again()

def main():
    welcome()

if __name__ == "__main__":
    main()