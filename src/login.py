from helper import *
import hashlib as hash
#define a function that allows for the creation of the account using the already exists checker to check for the user name already exists if so make them use a diffrent username, and if the username is admin
def create_account():
    username = input("What do you want your username to be")
    exist = exists("Documents\\user_info.csv", username)
    if exist == "yes":
        print("That username is available. ")
        clear_screen()
    else:
        print("There is already a user with that as ther name please try again")
        clear_screen()
        create_account()
    #get there password
    password = input("What do you want your password to be. ")
    #hash there password and save its value


#define a function that is called when the username is admin that allows for accounts to be removed


#define a function that edits the account csv removing or adding accounts to the user csv


#A function that prints the list of users for the admin and takes a input for which account they want to choose than deletes them


#A function to encrypt saved passwords with the hashlib library using a specific encryption 


#A function that shows the high scores for a game they choose and allows them to delete any of the high scores


#Define a function that checks if the password given is matched when hashed with that which is saved with the username


#Create a function that gets there username and uses the checking function to check if the username exists

