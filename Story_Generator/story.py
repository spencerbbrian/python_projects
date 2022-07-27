import imp
import random
from info import *

def welcome():
    global user
    print("Welcome to your story!\n")
    user = input("Please enter your name.\n")
    print(f"Welcome {user}. Are you ready to write your story?\n")
    print("[Yes] or [No]")
    game_start = input(f"Welcome {user}. Are you ready to write your story?\n Yes or No")
    if game_start in yes:
        story()
    else:
        quit()

def story():
    return