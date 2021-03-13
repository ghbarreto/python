print("==============================================")
print("")
print("Exercise 9-6 Icecream Stand ")

class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return print(f'Welcome to {self.name}, hope you like {self.cuisine_type} food.')

    
    def open_restaurant(self):
        return print("The restaurant is open")

class IceCreamStand(Restaurant):

    def __init__ (self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavours = ['Vanilla', 'Chocolate', 'Strawberry']

    def order(self):
        count = 1
        for i in self.flavours:
            fl = print(f"These are our flavours {i}")
    
        

order1 = IceCreamStand("Cactus Club", "American")
order1.order()

print("==============================================")
print("")
print("Exercise 9-7 Admin / 9-8 privileges ")

class User:

    def __init__ (self, first_name, last_name, email, gender, company_name, credit_card, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.company_name = company_name
        self.credit_card = int(credit_card)
        self.login_attempts = 0

    def describe_user(self):
        result = print(f"\nHello {self.first_name} {self.last_name}, your info: email - {self.email}\ngender - {self.gender}\ncompany - {self.company_name}\ncredit card - {self.credit_card}\n")
        return result

    def increment_login_attempts(self, login):
        self.login_attempts = login + 1
        return print(f"Login attempts: {self.login_attempts}")

    def reset_login_attempts(self, reset):
        reset = 0
        self.login_attempts = reset 
        return print(f"Login reset: {self.login_attempts}")

class Admin(User):

    def __init__(self, first_name, last_name, email, gender, company_name, credit_card, login_attempts):
        super().__init__(first_name, last_name, email, gender, company_name, credit_card, login_attempts)
        self.isAdmin = False
        self.privileges = Privileges()

class Privileges():
    
    def __init__(self, privileges="admin"):
        self.privileges = ["can delete", "can post", "can ban user"]

    
    def show_privileges(self):
        for i in self.privileges:
            print(f"an admin can: {i}")

    


user1 = Admin('Agretha','Foystone',"afoystone0@jimdo.com",'Female',"Leannon Inc", 4917514657728451, 2)
user1.privileges.show_privileges()

# user2 = User('Sim','Nerney',"snerney1@techcrunch.com",'Polygender',"Fadel Group",6763403784930265, 0)
# user3 = User('Shirleen','Dillestone','sdillestone2@ebay.co.uk','Agender','Hintz-Gerlach',4917344918206539, 0)
# user4 = User('Amitie','Magog',"amagog3@opensource.org",'Agender',"Stoltenberg, Glover and Schowalter", 4175006362041426, 0)
print("\n\n\n\n\n\n\n")
print("==============================================")
print("")
print("Exercise 9-9 Battery Upgrade ")
print("==============================================")

class Car:
    def __init__ (self, model, year, gas):
        self.model = model
        self.year = year
        self.gas = gas

    def introduction(self):
        return print(f"I know that your car is a {self.model} from {self.year}")

    def gasoline(self):
        if self.gas > 75:
            print(f"You dont need more gas")
        else:
            print(f"You need more gas")

class EletricCar(Car):
    def __init__ (self, model, year, gas):
        super().__init__(model, year, gas)
        self.battery = 100
        self.bat = Battery()

    def mileage(self):
        print(f"with that amount of battery ({self.battery}) you can run 300 km")

    def gasoline(self):
        print("Eletric cars don't have gasoline, dummy.")

class Battery:
    def __init__(self, battery="10"):
        self.battery = battery

    def batteryAge(self):
        print(f"Your battery will last {self.battery} years")

vehicle = EletricCar("Ferrari", 1995, 100)
vehicle.mileage()
vehicle.gasoline()

batteryCheck = Battery("100")
batteryCheck.batteryAge()

