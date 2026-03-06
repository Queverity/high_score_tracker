import os
import csv
import hashlib
from helper import clear_screen, exists
from game_data_parser import *
from games import *

# paths
USER_FILE = os.path.join("Documents", "user_info.csv")
SPECIAL_CHARACTERS = set("!@#$%^&*()-_=+[]{}|:;'<>.,?/~`")


def password_ok(password: str) -> bool:

    if len(password) < 12:
        return False

    if not any(c.islower() for c in password):
        return False

    if not any(c.isupper() for c in password):
        return False

    if not any(c.isdigit() for c in password):
        return False

    if not any(c in SPECIAL_CHARACTERS for c in password):
        return False

    return True


def hash_pw(item: str) -> str:
    sha256 = hashlib.sha256()
    sha256.update(item.encode("utf-8"))
    return sha256.hexdigest()


def user_exists(username: str) -> bool:
    return exists(USER_FILE, username)


def add_user(username: str, hashed: str) -> None:

    with open(USER_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f,
                                fieldnames=["username", "password",
                                            "poker_score", "slots_score",
                                            "blackjack_score"])
        writer.writerow({"username": username,
                         "password": hashed,
                         "poker_score": 0,
                         "slots_score": 0,
                         "blackjack_score": 0})


def create_account():
    # clear screen here
    clear_screen()

    while True:
        name = input("Choose a username: ").strip()

        if not name:
            print("Username cannot be blank.")
            continue

        if user_exists(name):
            print("That username is unavailable.")
            continue

        pw = input("Choose a password (12+ chars, upper, lower, digit, special): ")

        if not password_ok(pw):
            print("Password does not meet requirements.")
            continue
        add_user(name, hash_pw(pw))
        print("Account created.")
        break


def parse_user():
    return parse_user_info()


def user_display(users):

    for idx, u in enumerate(users, start=1):
        print(f"{idx}. {u['username']}")


#define a function that is called when the username is admin that allows for accounts to be removed
def admin():

    while True:
        print("To delete an account press 1\nTo exit press 2")
        action = input().strip()

        match action:

            case "1":
                # clear screen here
                clear_screen()
                users = parse_user()
                user_display(users)
                removing = input("Please input the number you want to delete. ").strip()

                if not removing.isdigit():
                    print(f"{removing} is not an option please try again")
                    continue
                idx = int(removing) - 1
                removed = remove(idx)

                if removed:
                    print(f"Removed account: {removed['username']}")

                else:
                    print(f"{removing} is not an option please try again")

            case "2":
                return

            case _:
                print("Invalid selection. Please try again.")

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
        
#A function that prints the list of users for the admin and takes a input for which account they want to choose than deletes them
def poker_display():
    user = parse_slots()

    for i in range(len(user)):
        print(f"{i+1}. {user[i]['username']}")
    user_num = int(input("What user do you want to delete? Please input only the number. "))
    return user_num


def remove(index):
    users = parse_user()

    if 0 <= index < len(users):
        removed = users.pop(index)
        save_user_info(users)
        return removed
    return None


def login(poker_scores,blackjack_scores,slots_scores):
    users = parse_user()
    name = input("What is your username? ").strip()
    pw = input("What is your password? ")
    hashed = hash_pw(pw)

    if name == "admin":

        if hashed == hash_pw("1234"):
            admin()

    for u in users:

        if u["username"] == name and u["password"] == hashed:
            print("Login successful.")
            continue_screen()
            clear_screen()
            overall_game_menu(name,poker_scores,blackjack_scores,slots_scores)
            return
    print("Invalid username or password.")
