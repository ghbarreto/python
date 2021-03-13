print("==============================================")
print("")
print("Exercise 8-1/2 Input names")

def greet(name):
    print(f"Hello, {name}")

# name = input("What is your name: ")
name = 'Gabriel'
greet(name)

print("==============================================")
print("")
print("Exercise 8-3 T-Shirt")

def tshirts(type, text):
    print(f"The tshirt type chosen is {type} and the text printed is {text}")

tshirts('V neck', 'I love life')
tshirts(text='I love my wife', type='Cupid')

print("==============================================")
print("")
print("Exercise 8-4 Large Tshirts")

def tshirtsize (size='large', message='I love python'):
    print(f"The tshirt size is {size} and the text is {message}")

tshirtsize()

print("==============================================")
print("")
print("Exercise 8-5 Cities")

def describe_city(cityName, countryName='Canada'):
    print(f"{cityName} is in {countryName}")

describe_city('Vancouver')
describe_city('Toronto')
describe_city('Salvador', countryName='Brazil')



