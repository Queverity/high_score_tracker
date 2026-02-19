#warrens helper function
import csv
#define a function that checks if something exists in a csv
def exists(location, search):
    try:
        with open(location, mode="r") as file:
            content = csv.reader(file)
            headers = next(content)
            rows = []
            for line in content:
                rows.append({headers[0]:line[0],headers[1]:line[1],headers[2]:line[2], headers[3]: line[3], headers[4]: line[4]})
    except:
        print("file does not exist. ")
    if search in rows:
        return "yes"
    else:
        return "I don't know what to say"
    
    
def clear_screen():
    print("\033c", end="")