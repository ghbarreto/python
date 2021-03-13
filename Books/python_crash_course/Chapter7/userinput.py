print("==============================================")
print("")
print("Exercise 7-1 Rental Car")

prompt = input('What kind of car do you want? ')
print(f'Let me see if we have the model {prompt}')

print("==============================================")
print("")
print("Exercise 7-2 Restaurant Seating")

p1 = input('How many people are in your dinner group? ')
val = int(p1)

if val >= 8:
    print('Sorry, you will have to wait for a table')
else:
    print('Please, follow me')

print("==============================================")
print("")
print("Exercise 7-3 Multiples of Ten")

p2 = input('Please, enter a number and I will tell you if it is divisible by 10 or not: ')
v = int(p2)

if v % 10 == 0:
    print(f"{v} is divisible by 10")
else:
    print(f"{v} is not divisible by 10")