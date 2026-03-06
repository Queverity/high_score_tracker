#Main Function for the High Score Tracker - PB, WG, DJ - 1st Period
#import all of the needed function from the helper file
from helper import *
from login import *
from games import *
from game_data_parser import *

#define the main menu function 
def menu(poker_scores,blackjack_scores,slots_scores):
    print("This is a High Score Manager program! It lets you play a few games, and saves the high scores you get from that game, both in your personal account for the program and in an all-time leaderboard if you're good enough.\nThe games currently devloped are slots and blackjack.\n")
    #use match case to determine what login function they are using and call it.

    while True:
        #give them there options
        print(f"If you want to login press 1. \nIf you want to login as Guest press 2.\nIf you want to create an account press 3.\nIf you want to exit press 4.\n")
        #get the option they need to use
        action = input().strip()

        match action:

            case "1":
                clear_screen()
                login(poker_scores,blackjack_scores,slots_scores)

            case "2":
                clear_screen()
                current_user = "Guest"
                overall_game_menu(current_user,poker_scores,blackjack_scores,slots_scores)

            case "3":
                clear_screen()
                create_account()

            case "4":
                clear_screen()
                exit()

            case _:
                clear_screen()
                print("That is an invalid answer. Please enter 1, 2, 3, or 4.")

menu(poker_scores,blackjack_scores,slots_scores)