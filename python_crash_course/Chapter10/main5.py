import json
import sys

filename = 'write/favourite.json'
            
def write_file(): 
    with open (filename, 'w') as file:
        username = input('Double checking your username: ')
        json.dump(username, file)


def check_file():
    ans = read_file()
    username = input('What is your password: ')
 
    if ans == username:
        print(f"Welcome back {ans}")  
    else:
        write_file()


def read_file():
    try:
        with open(filename) as file:
            ans = json.load(file)
            return ans
    except FileNotFoundError:
        return None
    else:
        return ans

check_file()