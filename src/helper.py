#warrens helper function
import csv
import sys
import time
#define a function that checks if a username exists in a csv (first column)
def exists(location, search):
    try:
        with open(location, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                # skip empty lines
                if row and row[0] == search:
                    return True
    except FileNotFoundError:
        print("file does not exist.")
    except Exception:
        # fallback for unexpected errors
        print("error reading file")
    return False
    
    
def clear_screen():
    print("\033c", end="")

def print_slow(text):

    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

    print()



def continue_screen():
    print_slow("Press Enter to continue.")
    input()