# CB 1st High Score Functions

# from game_data_parser import blackjack_scores,poker_scores,slots_scores

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
