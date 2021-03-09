print("==============================================")
print("")
print("Exercise 7-8 Deli")

sandwich_orders = ["Quarter pounder", "Big Mac", "Mc Chicken", "Triple Cheeseburger", "Hamburger", "Happy Meal"]
finished_sandwiches = []

print(f"These sandwiches are not ready: {sandwich_orders}")

for sandwich in sandwich_orders:
        print(f"Preparing your order of {sandwich}... ")

while sandwich_orders:  
    completed = sandwich_orders.pop()

    finished_sandwiches.append(completed)

for finished in finished_sandwiches:
    print(f"These sandwiches are ready: {finished}")

print("==============================================")
print("")
print("Exercise 7-9 No Pastrami")

list_sand = ["Pastrami", "Pastrami", "Pastrami", "Quarter pounder", "Big Mac", 
            "Mc Chicken", "Triple Cheeseburger", "Hamburger", "Happy Meal"]

newMenu = []

print("The deli has ran out of pastrami")

while "Pastrami" in list_sand:
    list_sand.remove("Pastrami")

print(f"The new menu is {list_sand}")

print("==============================================")
print("")
print("Exercise 7-10 Dream Vacation")

vacation = {}
loop = True
asking = True


while loop:
    user = input("What is your name: ")
    dreamVacation = input("What is your dream vacation: ")

    vacation[user] = dreamVacation

    continues = input("Do you want to continue? y/n :")

    if continues == 'y':
        continue
    elif continues == 'n':
        break
    
    if continues is not 'n' or 'y':
        a = input("Please, either [y/n] :")    
    elif a == 'y':
        continue
    elif a == 'n':
        break
    else:
        print("Wrong digits, I will terminate, thanks. ")  
        break

for item1, item2 in vacation.items():
    print(f"{item1}'s favourite destination is {item2}")
