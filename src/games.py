# DJ 1st Games
from helper import *
from high_score_functions import personal_highs_printer,personal_highs_setter,overall_highs_menu,overall_highs_setter,high_score_sorter,high_score_writing

from game_data_parser import slots_scores,blackjack_scores,user_info


def overall_game_menu(username):
    while True:
        print("What would you like to do?\n1. View Personal High Scores\n2. View All-Time High Scores\n3. Play Games\n4. Exit")
        action = input("Enter Number:\n").strip().lower()
        match action:
            case "1":
                personal_highs_printer(username,user_info)
                pass
            case "2":
                overall_highs_menu(blackjack_scores,slots_scores)
                pass
            case "3":
                # go to game menu function
                pass
            case "4":
                print("Are you sure you want to exit?")
                exit = input("Y/N:\n").strip().upper()
                if exit == "Y":
                    # save all high scores to their files, make sure everything is saved
                    print("Goodbye!")
                    return
                else:
                    continue
            case _:
                print("Please enter 1, 2, 3, or 4.")
                continue

def game_menu():
    while True:
        print("What game would you like to play?\n1. Slots\n2. Blackjack\n3. Exits")
        game = input("Enter number:\n").strip().capitalize()
        match game:
            case "1":
                # run slots game
                # go through all the high score finding and sorting stuff
                # ask if user would like to continue playing other games
                pass
            case "2":
                # run blackjack game
                # go through all the high score finding and sorting stuff
                # ask if user would like to continue playing other games
                pass
            case "3":
                clear_screen()
                exit()
            case _:
                print("Please enter 1 or 2.")
                continue
