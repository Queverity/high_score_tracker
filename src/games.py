# DJ 1st Games

def overall_game_menu():
    while True:
        print("What would you like to do?\n1. View Personal High Scores\n2. View All-Time High Scores\n3. Play Games\n4. Exit")
        action = input("Enter Number:\n").strip().lower()
        match action:
            case "1":
                # call personal high score function from pryor's files
                pass
            case "2":
                # call overall high scores function from pryor's files
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

def game_menu():
    while True:
        print("What game would you like to play?\n1. Slots\n2. Blackjack")
        game = input("Enter number:\n").strip().capitalize()
        match game:
            case "1":
                # run slots game
                # go through all the high score finding and sorting stuff
                # ask if user would like to continue playing other games
                pass
            case "2":
                # run slots game
                # go through all the high score finding and sorting stuff
                # ask if user would like to continue playing other games
                pass
            case _:
                print("Please enter 1 or 2.")
                continue
