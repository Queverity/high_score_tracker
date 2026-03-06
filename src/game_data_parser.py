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
    with open("Documents//blackjack_scores.csv",mode="r",newline='') as scores:
        fieldnames = ['username','high_score']
        reader = csv.DictReader(scores,fieldnames)
        blackjack_scores = []
        for row in reader:
            if 'username' in row['username']: 
                pass
            else:
                blackjack_scores.append(row)

        for row in blackjack_scores:
            row['high_score'] = int(row['high_score'])
    return blackjack_scores

def parse_poker():
    with open("Documents//poker_scores.csv",mode="r",newline='') as scores:
        fieldnames = ['username','high_score']
        reader = csv.DictReader(scores,fieldnames)
        poker_scores = []
        for row in reader:
            if 'username' in row['username']: 
                pass
            else:
                poker_scores.append(row)
        
        for row in blackjack_scores:
            row['high_score'] = int(row['high_score'])
    return poker_scores

def parse_slots():
    with open("Documents//slots_scores.csv",mode="r",newline='') as scores:
        fieldnames = ['username','high_score']
        reader = csv.DictReader(scores,fieldnames)
        slots_scores = []
        for row in reader:
            if 'username' in row['username']: 
                pass
            else:
                slots_scores.append(row)

        for row in blackjack_scores:
            row['high_score'] = int(row['high_score'])
    return slots_scores

def parse_user_info():
    with open("Documents//user_info.csv",mode="r",newline='') as userinfo:
        fieldnames = ['username','password','poker_score','slots_score','blackjack_score']
        reader = csv.DictReader(userinfo,fieldnames)
        user_info = []
        for row in reader:
            # skip header row and any empty lines
            if not row.get('username') or row.get('username').lower() == 'username':
                continue
            user_info.append(row)
    return user_info

def save_score_files(file_path,data):
    with open(file_path,mode="w",newline="") as file:
        fieldnames = ['username','high_score']
        first_row = {'username':'username','high_score':'high_score'}
        writer = csv.DictWriter(file,fieldnames)

        writer.writerow(first_row)
        
        for i in data:
            writer.writerow(i)

def save_user_info(data):
    with open("Documents//user_info.csv",mode="w") as user_info:
        fieldnames = ['username','password','poker_score','slots_score','blackjack_score']       
        first_row = {'username':'username','password':'password','poker_score':'poker_score','slots_score':'slots_score','blackjack_score':'blackjack_score'}
        writer = csv.DictWriter(user_info,fieldnames)

        writer.writerow(first_row)
        for i in data:
            writer.writerow(i)     

    


blackjack_scores = parse_blackjack()
poker_scores = parse_poker()
slots_scores = parse_slots()
user_info = parse_user_info()


