# DJ 1st Games

from high_score_functions import personal_highs_printer,personal_highs_setter,overall_highs_menu,overall_highs_setter,high_score_sorter,high_score_writing

from game_data_parser import slots_scores,blackjack_scores,poker_scores,user_info,save_score_files,save_user_info

from slots import slots_main

from blackjack import game

def game_menu(slots_scores,blackjack_scores,current_user):
    while True:
        print("What game would you like to play?\n1. Slots\n2. Blackjack")
        game = input("Enter number:\n").strip().capitalize()
        match game:
            case "1":
                high_score = slots_main()
                slots_scores = overall_highs_setter(current_user,high_score,slots_scores)
                slots_scores = high_score_sorter(game,blackjack_scores,poker_scores,slots_scores)
                continue_playing = input("Would you like to play other games? Y/N: \n").strip().capitalize()
                if continue_playing == "Y":
                    continue
                else:
                    return slots_scores,blackjack_scores
            case "2":
                high_score = game()
                blackjack_scores = overall_highs_setter(current_user,high_score,blackjack_scores)
                blackjack_scores = high_score_sorter(game,blackjack_scores,poker_scores,slots_scores)
                continue_playing = input("Would you like to play other games? Y/N: \n").strip().capitalize()
                if continue_playing == "Y":
                    continue
                else:
                    return slots_scores,blackjack_scores
            case _:
                print("Please enter 1 or 2.")
                continue

def overall_game_menu(current_user):
    while True:
        print("What would you like to do?\n1. View Personal High Scores\n2. View All-Time High Scores\n3. Play Games\n4. Exit")
        action = input("Enter Number:\n").strip().lower()
        match action:
            case "1":
                personal_highs_printer(current_user,user_info)
                pass
            case "2":
                overall_highs_menu(blackjack_scores,slots_scores)
                pass
            case "3":
                slots_scores,blackjack_scores = game_menu(slots_scores,blackjack_scores,current_user)
                pass
            case "4":
                print("Are you sure you want to exit?")
                exit = input("Y/N:\n").strip().upper()
                if exit == "Y":
                    save_score_files("Documents\slots_scores.csv",slots_scores)
                    save_score_files("Documents\\blackjack_scores.csv",blackjack_scores)
                    save_user_info(user_info)
                    print("Goodbye!")
                    return
                else:
                    continue
            case _:
                print("Please enter 1, 2, 3, or 4.")
                continue