
print("==============================================")
print("")
print("Exercise 9-4 Number Served ")

class Restaurant:

    def __init__(self, name, cuisine_type, number_served):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 2

    def describe_restaurant(self):
        return print(f'Welcome to {self.name}, hope you like {self.cuisine_type} food, we have {self.number_served} clients waiting.')

    def restaurants(self, num_of_customers):
        num_of_customers += self.number_served
        return print(f"The restaurant has served {num_of_customers}")

    def restaurantUpdate(self, new_customers):
        new_customers += self.number_served
        return new_customers

    def open_restaurant(self):
        return print("The restaurant is open")

client = Restaurant("Cactus Club", "American", "12")
client.restaurants(15)
print(client.describe_restaurant())

client2 = Restaurant("McDonald's", "American", '15')
client3 = Restaurant("Marechal", "Brazilian", '19')

print("==============================================")
print("")
print("Exercise 9-5 Login Attempts ")

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


user1 = User('Agretha','Foystone',"afoystone0@jimdo.com",'Female',"Leannon Inc", 4917514657728451, 0)
user2 = User('Sim','Nerney',"snerney1@techcrunch.com",'Polygender',"Fadel Group",6763403784930265, 0)
user3 = User('Shirleen','Dillestone','sdillestone2@ebay.co.uk','Agender','Hintz-Gerlach',4917344918206539, 0)
user4 = User('Amitie','Magog',"amagog3@opensource.org",'Agender',"Stoltenberg, Glover and Schowalter", 4175006362041426, 0)

user1.describe_user()
user1.increment_login_attempts(12)
user1.reset_login_attempts(10)
# user2.describe_user()
# user3.describe_user()
# user4.describe_user()

