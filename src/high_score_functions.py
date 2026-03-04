# CB 1st High Score Functions

import csv
from game_data_parser import *

# define function personal_highs_printer(user_info,current_user):
    # ask user if they would like to view poker, slots, or blackjack high scores
    # display their high score for that game
    # ask if user would like to view other scores, if yes, then continue, if no, return

# define function personal_highs_setter(user_info,current_user,new_score):
    # check which game the user just finished
    # compare the score they just got in the game to the saved high score in the user_info file
    # if there is no score, set the score in user_info file to the new_score, display 'New High Score!'
    # if new score is lower, do nothing
    # if new score is higher, set the score in user_info file to the new_score, display 'New High Score!'
    # return to game menu

# define function overall_highs_menu(user_info,current_user,game_data files):
    # ask user which game they would like to view the top high scores for
    # access that high score file, print the Top 10 high scores
    # ask user if they would like to continue viewing the high scores
    # if yes, continue, if no, return

# define function overall_highs_setter(user_info,current_user,game_data files,new_score):
    # check which game the user just completed
    # iterate through the high scores of that game, check the highest score that the new_score is higher than (if any)
    # replace that score with the new_score
    # if new_score isn't higher than any of the scores in the list, do nothing
    # print Top 5 high scores

# define high_score_sorter(current_game,game_data files)
    # check which game just finished
    # grab those scores, put them into this piece of code
    # sorted_scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)} this sorts the scores high to low
    # iterate through the sorted_scores list, setting each item in the list to its position in the high score file

# define high_score_writing(scores,game_file_path):
    # clear the game file that we'll be writing to
    # use DictWriter to write each pair from user_scores to the game file

def high_score_writing(user_scores,game_file_path):
    with open(game_file_path,mode="w") as game:
        pass

    with open(game_file_path,mode="a",newline="") as game:
        fieldnames = ['username','score']
        dict_writer = csv.DictWriter(game,fieldnames)
        for pair in user_scores:
            dict_writer.writerow(pair)

def personal_highs_printer(current_user,user_info):
    if current_user == "Guest": 
        print("You are a guest, and thus your personal high scores are not saved. Perhaps make an account?")
        return
    else:
        for i in user_info:
            if i['username'] == current_user:
                print(f"Poker High Score: {i['poker_score']}\nSlots High Score: {i['slots_score']}\nBlackjack High Score: {i['blackjack_score']}")
                return

def personal_highs_setter(current_user,user_info,new_score,game):
    if current_user == "Guest": return
    match game:
        case 'Poker':
            for i in user_info:
                if i['username'] == current_user:
                    if i['poker_score'] < new_score:
                        i['poker_score'] == new_score
                        return
                    else:
                        return
        case 'Slots':
            for i in user_info:
                if i['username'] == current_user:
                    if i['slots_score'] < new_score:
                        i['slots_score'] == new_score
                        return
                    else:
                        return
        case 'Blackjack':
            for i in user_info:
                if i['username'] == current_user:
                    if i['blackjack_score'] < new_score:
                        i['blackjack_score'] == new_score
                        return
                    else:
                        return
        case _:
            print("Unexpected error")
            return

def overall_highs_menu(poker_scores,blackjack_scores,slots_scores):
    def top_ten_printer(mode):
        count = 0
        for row in mode:
            if count == 10:
                return
            else:
                count += 1
                print(f"{count}. {row['username']}: {row['score']}")
    while True:
        game = input("Would you like to view high scores for Poker, Slots, or Blackjack?\n1. Slots\n2. Blackjack\nEnter Number:\n").strip()
        match game:
            case "1":
                top_ten_printer(mode=slots_scores)
            case "2":
                top_ten_printer(mode=blackjack_scores)
            case _:
                print("Please enter 1, or 2.")
                continue
        viewing = input("Would you like to view other high scores? Y/N").strip().capitalize()
        if viewing == "Y":
            continue
        else:
            break

def overall_highs_setter(current_user,new_score,game_scores):
    new_score = int(new_score)
    for i in game_scores:
        for name,score in i.items():
            if new_score > score:
                name = current_user
                score = new_score
                print("You have set a new high score! View overall high scores in the main menu to see where you stand on the leaderboard.")
                return game_scores
            else:
                pass
    return game_scores
            
def high_score_sorter(game,blackjack_scores,poker_scores,slots_scores):
    def sorter_code(scores):
        sorted_scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}
        return sorted_scores
    while True:
        match game:
            case "Blackjack":
                sorted_scores = sorter_code(blackjack_scores)
                high_score_writing(sorted_scores,'Documents//blackjack.py')
                return
            case "Poker":
                sorted_scores = sorter_code(poker_scores)
                high_score_writing(sorted_scores,'Documents//poker.py')
                return
            case "Slots":
                sorted_scores = sorter_code(slots_scores)
                high_score_writing(sorted_scores,'Documents//slots.py')
                return
            case _:
                print(f"Unexpected value: {game}")
