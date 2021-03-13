import json

numbers = [2, 3, 5, 8, 10, 12, 25]

filename = 'write/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

with open(filename) as fr:
    print(json.load(fr))

print("========================================")

# username = input('What is your name: ')

# file = 'username.json'
# with open(file, 'w') as usr:
#     json.dump(username, usr)
#     print(f"We will rememver you when you come back, {username}")

# with open(file) as read_usr:
#     answer = json.load(read_usr)
#     print(f"Hello {answer}")

print("========================================")


def get_stored_username():
    try_file = 'write/tryblock.json' 
    try: 
        with open(try_file) as f:
            pron = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return pron

def get_new_username():
    pron = input("What is your name: ")
    try_file = 'write/tryblock.json'
    
    with open(try_file, 'w') as f:
        json.dump(pron, f)
        print(f"We will remember you when you come back, {pron}")
    return pron


def greet():
    pron = get_stored_username()

    if pron:
        print(f"Welcome back, {pron}")
    else:
        pron = get_new_username()       

greet()


print("========================================")