#Main Function for the High Score Tracker - PB, WG, DJ - 1st Period
#import all of the needed function from the helper file
from helper import *
from login import *
from games import *
#define the main menu function 
def menu():
    #use match case to determine what login function they are using and call it.
    while True:
        #give them there options
        print(f"If you want to login press 1. \nIf you want to login as Guest press 2.\nIf you want to create an account press 3.\nIf you want to exit press 4.\n")
        #get the option they need to use
        action = input()
        match action:
            case "1":
                clear_screen
                login()
            case "2":
                game_menu()
            case "3":
                clear_screen
                create_account()
            case "4":
                clear_screen
                exit()