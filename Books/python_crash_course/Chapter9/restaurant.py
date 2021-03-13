print("==============================================")
print("")
print("Exercise 9-1 Restaurant")

class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return print(f'Welcome to {self.name}, hope you like {self.cuisine_type} food.')

    
    def open_restaurant(self):
        return print("The restaurant is open")

client = Restaurant("Cactus Club", "American")
client2 = Restaurant("McDonald's", "American")
client3 = Restaurant("Marechal", "Brazilian")

print("==============================================")
print("")
print("Exercise 9-2 Three Restaurants")

client.open_restaurant()
client.describe_restaurant()

client2.open_restaurant()
client2.describe_restaurant()

client3.open_restaurant()
client3.describe_restaurant()

print("==============================================")
print("")
print("Exercise 9-3 Users")

class User:

    def __init__ (self, first_name, last_name, email, gender, company_name, credit_card):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.company_name = company_name
        self.credit_card = int(credit_card)

    def describe_user(self):
        result = print(f"\nHello {self.first_name} {self.last_name}, your info: email - {self.email}\ngender - {self.gender}\ncompany - {self.company_name}\ncredit card - {self.credit_card}")
        return result


user1 = User('Agretha','Foystone',"afoystone0@jimdo.com",'Female',"Leannon Inc", 4917514657728451)
user2 = User('Sim','Nerney',"snerney1@techcrunch.com",'Polygender',"Fadel Group",6763403784930265)
user3 = User('Shirleen','Dillestone','sdillestone2@ebay.co.uk','Agender','Hintz-Gerlach',4917344918206539)
user4 = User('Amitie','Magog',"amagog3@opensource.org",'Agender',"Stoltenberg, Glover and Schowalter", 4175006362041426)

user1.describe_user()
user2.describe_user()
user3.describe_user()
user4.describe_user()