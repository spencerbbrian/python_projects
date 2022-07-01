### PYTHON PROJECTS
This is a repository for all projects I have worked on to improve my python skills a developer.
Below is a list of all the projects in this repo.
1. Guess_the_number.
    # Instructions
    This is a simple guessing game where there is a random number generated from a range depending on the game difficulty(easy, intermediate or hard). If the input value for the game level or guess is not accounted for, an error message shows up. For every level a specific number of attempts are allowed that you can keep guessing else it's game over. All three levels have been divided into three different functions with separate while loops so I could easily debug every level. The game also includes hints for when the number guessed is higher or lower than the random number that has been generated for the game level.
    {
        if guess == easy_game_number:
            print("Congratulations you beat the game")
        else:
            print("Sorry, you've run out of guesses")
            print(f"Also the right answer was {easy_game_number}")
    }
    Depending on wether the user gets the guess right or runs out of attempts, the game comes to an end and the right answer is displayed.