## PYTHON PROJECTS
This is a repository for all projects I have worked on to improve my python skills as a developer.
Below is a list of all the projects in this repo.
1. ## Guess The Number.
    This is a simple guessing game where there is a random number generated from a range depending on the game difficulty(easy, intermediate or hard). If the input value for the game level or guess is not accounted for, an error message shows up. For every level a specific number of attempts are allowed that you can keep guessing else it's game over. All three levels have been divided into three different functions with separate while loops so I could easily debug every level. The game also includes hints for when the number guessed is higher or lower than the random number that has been generated for the game level.<br>
    {<br>
        if guess == easy_game_number:<br>
            print("Congratulations you beat the game")<br>
        else:<br>
            print("Sorry, you've run out of guesses")<br>
            print(f"Also the right answer was{easy_game_number}")<br>
    }<br>
    Depending on wether the user gets the guess right or runs out of attempts, the game comes to an end and the right answer is displayed.

2. ## ROLLING DICE SIMULATOR
    Yet another simple game but takes than an hour to complete. In this game a user just enters yes or no to roll the die or quit the game respectively. If the user enters yes, randint is used to print a random integer from 1 to 6. The game has two levels; one for a single die roll and another for a dice roll which returns a sum of the dice.

3. ## HANGMAN
    After eight rounds of coffee and a lot of copy and pasting and some modification of course. I finished the hangman game. Trust, I thought I would bail on this. Anyway, it's your regular hangman game with some words which are just two in this case apple and orange. The basic functionality of the game being able to detect a letter and pass it as a guess and crosscheck with the random word selected is working fine. Also being able to replace the a letter than still needs guessing is an added functionality.