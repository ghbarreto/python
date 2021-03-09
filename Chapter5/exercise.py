usernames = ["admin", "thaisyu", "ghbarreto", "leeloo", "renarose"]

print("Exercise 5-8")
for username in usernames:
    if username == "admin":
        print (f"Welcome {username}, do you wish to edit the webserver?")
    else:   
        print (f"Welcome {username}")

print("=================================================================================")

print("Exercise 5-9")
for username in usernames:
    usr = usernames.remove(username)  
if usr:
    print(f"We have a few users {usr}")
else:
    print(f"We have no users {usr}")

print("=================================================================================")

print("Exercise 5-10")

current_users = ["Leeloo", "admin", "ghbarreto", "thaisyu", "renegade"]
new_users = ["leeloo", "admin", "gabriel", "paulo", "rose"]
current_user = []
newusr = []

for x in current_users:
    current_user.append(x.lower())

for y in new_users:
    newusr.append(y.lower())

for newusr in new_users:
    if newusr in current_user:
        print(f"Your username is not available {newusr}")
    else:
        print(f"Your username is available {newusr}")

        
print("=================================================================================")

print("Exercise 5-11")

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in myList:
    if x == 1:
        print(f"{x}st")
    elif x == 2:
        print(f"{x}nd")
    elif x == 3:
        print(f"{x}rd")
    else:
        print(f"{x}th")