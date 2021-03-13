print("==============================================")
print("")
print("Exercise 7-4 Pizza Toppingsx")

active = True

while active:
    question = input("What are your desired toppings: \n To exit, type exit: \n ====================== :")  
    
    if question == "exit":
        active = False
    else:
        print(f"I will add {question} to your pizza")

print("==============================================")
print("")
print("Exercise 7-5 Movie Tickets")

movieLoop = True

while movieLoop:
    age = input("To exit type exit \nPlease, enter your age: ")
    
    if age == "exit":
        print("Thank you for buying with us :)")
        break

    ageInt = int(age)

    if ageInt <= 3:
        print(f"I see that you are {ageInt} years old, so your ticket will be for free")
    elif ageInt <= 12:
        print(f"Your ticket will be $10")
    else:
        print(f"Your ticket will be $15")


print("==============================================")
print("")
print("Exercise 7-2 Restaurant Seating")
        
act = True

while act:
    print("Thais eu te amo")
    


