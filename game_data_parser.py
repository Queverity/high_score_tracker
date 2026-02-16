# CB 1st Game Parsing Function

import csv

# define function parse_blackjack():
    # Here, we're opening the file, using DictReader to turn each row into a dictionary, then appending each of those dictionaries to the blackjack_scores list. After that, we return the blackjack_scores list.
    # with open("game_data\blackjack_scores.csv",mode="r",newline='') as scores:
        # fieldnames = ['username','score']
        # reader = csv.DictReader(scores,fieldnames)
        # blackjack_scores = []
        # for row in reader:
            # blackjack_scores.append(row)
    # return blackjack_scores

# define function parse_poker():
    # Here, we're opening the file, using DictReader to turn each row into a dictionary, then appending each of those dictionaries to the poker_scores list. After that, we return the poker_scores list.
    # with open("game_data\poker_scores.csv",mode="r",newline='') as scores:
        # fieldnames = ['username','score']
        # reader = csv.DictReader(scores,fieldnames)
        # poker_scores = []
        # for row in reader:
            # poker_scores.append(row)
    # return poker_scores

# define function parse_slots():
    # Here, we're opening the file, using DictReader to turn each row into a dictionary, then appending each of those dictionaries to the slots_scores list. After that, we return the slots_scores list.
    # with open("game_data\slots_scores.csv",mode="r",newline='') as scores:
        # fieldnames = ['username','score']
        # reader = csv.DictReader(scores,fieldnames)
        # slots_scores = []
        # for row in reader:
            # slots_scores.append(row)
    # return slots_scores

# blackjack_scores = parse_blackjack()
# poker_scores = parse_poker()
# slots_scores = parse_slots()

def parse_blackjack():
    with open("blackjack_scores.csv",mode="r",newline='') as scores:
        fieldnames = ['username','score']
        reader = csv.DictReader(scores,fieldnames)
        blackjack_scores = []
        for row in reader:
            blackjack_scores.append(row)
    return blackjack_scores

def parse_poker():
    with open("poker_scores.csv",mode="r",newline='') as scores:
        fieldnames = ['username','score']
        reader = csv.DictReader(scores,fieldnames)
        poker_scores = []
        for row in reader:
            poker_scores.append(row)
    return poker_scores

def parse_slots():
    with open("slots_scores.csv",mode="r",newline='') as scores:
        fieldnames = ['username','score']
        reader = csv.DictReader(scores,fieldnames)
        slots_scores = []
        for row in reader:
            slots_scores.append(row)
    return slots_scores

blackjack_scores = parse_blackjack()
poker_scores = parse_poker()
slots_scores = parse_slots()

for i in blackjack_scores:
    print(f"{i['username']}: {i['score']}")