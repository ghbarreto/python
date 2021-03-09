print("==============================================")
print("")
print("Exercise 8-12 Sandwiches")

def sandwich(*items):
    
    result = print(f"{items}")
    return result

sandwichMaker = True

sandwich('Pao com gergilim, ketchup, hamburger, ovo')

print("==============================================")
print("")
print("Exercise 8-13 Build profile")

def profile(firstName, lastName, **args):
    print(f"{firstName} {lastName}")
    for a, z in args.items():
        print(f"- {a}: {z}")

profile(lastName='Barreto', firstName='Gabriel', age=26, height="6'3", relationship="married")
profile(lastName='Barreto', firstName='Thais', age=32, height="5'10", relationship="married")
profile(lastName='Barreto', firstName='Rose', age=53, height="5'7", relationship="married")

print("==============================================")
print("")
print("Exercise 8-14 Cars")

def car_info(manufacturer, modelName, **val):
    ans = print(f"\nManufacturer: {manufacturer}\nModel: {modelName}")
    for s, v in val.items():
        print(f"- {s}: {v}")
    

car_info(manufacturer= 'Ferrari', modelName= 'LaFerrari', color="Red", price="3.5m", towPackage = True)
car_info(manufacturer= 'Lamborghini', modelName= 'Aventador', color="Black", price="500k", towPackage = False)
car_info(manufacturer= 'Ford', modelName= 'Ka', color="White", price="10k", towPackage = True)

