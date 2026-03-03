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
                         "poker_score": "",
                         "slots_score": "",
                         "blackjack_score": ""})


def create_account():
    while True:
        clear_screen()
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


def user_display():
    users = parse_user()
    for idx, u in enumerate(users, start=1):
        print(f"{idx}. {u['username']}")
    try:
        with open("Documents\\user_info.csv",mode="w") as users:
            users.write
    except:
        print("The thingy didn't work.")
#define a function that is called when the username is admin that allows for accounts to be removed
def admin():
    print("To delete an account press 1\nTo delete a high score press 2\nTo exit press 3")
    action = input()
    match action:
        case "1":
            user_display()
            removing = input("Please input the number you want to delete. ")
            remove(accounts[removing-1])

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
        print(f"{i+1}. {user[i]["username"]}")
    user_num = int(input("What user do you want to delete? Please input only the number. "))
    return user_num


#Create a function that gets there username and uses the checking function to check if the username exists
def login(user_info):
    while True:
        username = input("What is your username? ")
        exists = exists("Documents//user_info.csv",username)

        if exists == "yes":

            for i in user_info:
                pass

"""def admin():
    print("1) delete account\n2) exit")
    action = input().strip()
    if action == "1":
        idx = user_display()
        if idx is not None:
            remove(idx)"""


def login():
    users = parse_user()
    name = input("What is your username? ").strip()
    pw = input("What is your password? ")
    hashed = hash_pw(pw)
    for u in users:
        if u["username"] == name and u["password"] == hashed:
            print("Login successful.")
            game_menu()
            return
    print("Invalid username or password.")