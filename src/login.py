from helper import *
import hashlib as hash
import string
#define a function that allows for the creation of the account using the already exists checker to check for the user name already exists if so make them use a diffrent username, and if the username is admin

special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ":", ";", "'", "<", ">", ",", ".", "?", "/", "`", "~"]

def password_requirements(password):
    if len(password) < 12:
        print("Your password is not long enough.")
        return
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
                                return
                            else:
                                pass
                        print("You need a number in your password.")
                    else:
                        pass
                print("You need an uppercase letter in your password.")
                return
            else:
                pass
        print("You need a lowercase letter in your password.") 
        return

def create_account():
    username = input("What do you want your username to be")
    exist = exists("Documents\\user_info.csv", username)
    if exist == "yes":
        print("That username is available. ")
        clear_screen()
    else:
    #get their password
        password = input("What do you want your password to be? It needs to be at least 12 characters long and have a lowercase letter, an uppercase letter, a number, and a special character.")
    #hash there password and save its value

def user_login(user_info):
    while True:
        username = input("Enter your username, or type 'exit' to go back to main menu:\n").strip()
        if username.lower() == 'exit':
            return
        else:
            for i in user_info:
                if i['username'].lower() == username.lower():
                    password = input(f"Please enter your password {username}:\n").strip()
                    # We'll need to set up the password checker to work properly with the hashlib library.
                    # if the password is correct, move onto the game menu
                    pass
        print("Cannot find that username, either enter a valid one or make a new account")
        continue
#define a function that is called when the username is admin that allows for accounts to be removed


#define a function that edits the account csv removing or adding accounts to the user csv


#A function that prints the list of users for the admin and takes a input for which account they want to choose than deletes them


#A function to encrypt saved passwords with the hashlib library using a specific encryption 


#A function that shows the high scores for a game they choose and allows them to delete any of the high scores for admin


#Define a function that checks if the password given is matched when hashed with that which is saved with the username


#Create a function that gets there username and uses the checking function to check if the username exists

