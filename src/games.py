# DJ 1st Games

from high_score_functions import personal_highs_printer,personal_highs_setter,overall_highs_menu,overall_highs_setter,high_score_sorter,high_score_writing

from game_data_parser import slots_scores,blackjack_scores,poker_scores,user_info

from slots import slots_main


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
                    break
            case "2":
                # run blackjack game
                # go through all the high score finding and sorting stuff
                # ask if user would like to continue playing other games
                pass
            case _:
                print("Please enter 1 or 2.")
                continue
