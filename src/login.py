from helper import *
import hashlib as hash
import string
#define a function that allows for the creation of the account using the already exists checker to check for the user name already exists if so make them use a diffrent username, and if the username is admin

special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ":", ";", "'", "<", ">", ",", ".", "?", "/", "`", "~"]

def password_requirements(password, username):
    if len(password) < 12:
        print("Your password is not long enough.")
        passwords(username)
    else:
        for i in password:
            if i in string.ascii_lowercase:
                for a in password:
                    if a in string.ascii_uppercase:
                        for b in password:
                            if b in string.digits:
                                for c in password:
                                    if c in special_characters:
                                        return True
                                    else:
                                        pass
                                print("You need a special character in your password.")
                                passwords(username)
                            else:
                                pass
                        print("You need a number in your password.")
                    else:
                        pass
                print("You need an uppercase letter in your password.")
                passwords(username)
            else:
                pass
        print("You need a lowercase letter in your password.") 
        passwords(username)

def create_account():
    account = {}
    usernames = input("What do you want your username to be")
    exist = exists("Documents\\user_info.csv", usernames)
    if exist == "yes":
        print("That username is unavailable. ")
        clear_screen()
        create_account()
    else:
        account["username"] = usernames
        passwords(usernames)

#make a function that gets there password and hashes it
def passwords(username):
 #get their password
        password = input("What do you want your password to be? It needs to be at least 12 characters long and have a lowercase letter, an uppercase letter, a number, and a special character.")
        password_requirements(password, username)
    #hash there password and save its value
        password = hashing(password)

#A function that parses the account function
def parse_user():
    with open("Documents\\user_info.csv",mode="r",newline='') as scores:
        fieldnames = ['username','score']
        reader = csv.DictReader(scores,fieldnames)
        users = []
        for row in reader:
            users.append(row)
    return users

#A function that prints the list of users for the admin and takes a input for which account they want to choose than deletes them
def user_display():
    user = parse_user()
    for i in range(len(user)):
        print(f"{i+1}. {user[i]["username"]}")
    user_num = int(input("What user do you want to delete? Please input only the number. "))
    return user_num

#define a function that is called when the username is admin that allows for accounts to be removed
def admin():
    user_num = user_display()
    


#define a function that edits the account csv removing or adding accounts to the user csv
def add(username, password):
    with open("Notes/sample.csv", 'r+', newline='') as csvfile:
        feildnames = ["username", "password"]
        reader=csv.reader(csvfile)
        for line in reader:
            print(f"{feildnames[0]}, {line[0]} favorite color {line[1]}")
        writer = csv.DictWriter(csvfile, fieldnames=feildnames)
        #writer.writeheader()
        writer.writerow({'username':username, 'password':password})
        

#A function that shows the high scores for a game they choose and allows them to delete any of the high scores
def parse_blackjack():
    with open("Documents//blackjack_scores.csv",mode="r",newline='') as scores:
        fieldnames = ['username','score']
        reader = csv.DictReader(scores,fieldnames)
        blackjack_scores = []
        for row in reader:
            blackjack_scores.append(row)
    return blackjack_scores

def parse_poker():
    with open("Documents//poker_scores.csv",mode="r",newline='') as scores:
        fieldnames = ['username','score']
        reader = csv.DictReader(scores,fieldnames)
        poker_scores = []
        for row in reader:
            poker_scores.append(row)
    return poker_scores

def parse_slots():
    with open("Documents//slots_scores.csv",mode="r",newline='') as scores:
        fieldnames = ['username','score']
        reader = csv.DictReader(scores,fieldnames)
        slots_scores = []
        for row in reader:
            slots_scores.append(row)
    return slots_scores

#Define a function that checks if the password given is matched when hashed with that which is saved with the username
def hash_check(password):
    sha256 = hash.sha256()
    sha256.update(password)
    return sha256.hexdigest()

#Create a function that gets there username and uses the checking function to check if the username exists
def login():
    username = input("What is your username? "):
    

#A function that hashes a string
def hashing(item):
    sha256 = hash.sha256()
    sha256.update(item)
    return sha256.hexdigest()