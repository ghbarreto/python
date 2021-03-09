favourite_numbers = {
    'thais' : 6,
    'gabriel' : 6,
    'Rose': 7,
    'Paulo': 1
}
print(" ")
print("Exercise 6-4")
for key, values in favourite_numbers.items():
    print(f"Hello {key}, your favourite number is {values}")

print(" ")
print("==============================================")
print(" ")
programming = {
    'variable' : 'in a variable, you can store any type of value to be accessed later.',
    'function' : 'functions are smaller pieces of codes that can be called to perform an action.',
    'loops' : 'loops are used to display all the values assigned in a variable.',
    'array' : 'arrays are variables with multiple values.',
    'dataset' : 'datasets is a collection of data ',
}

for key, values in programming.items():
    print(f"{key}: {values} ")

print("==============================================")
print("")
print("Exercise 6-5 Rivers ")

rivers = {
    'Nile' : 'Egypt',
    'Amazon River': 'Brazil',
    'Mississippi River': 'USA'
}

rivers_description = {
    'Nile' : 'Runs through Egypt',
    'Amazon River' : 'Runs through Brazil',
    'Mississippi River' : 'Runs through the USA'
}

rivers_selected = ['Nile', 'Amazon River', 'Mississippi River']

for key, values in rivers.items():
    if key in rivers_selected:
        rivers_ = rivers_description[key].title()
        print(f"The {key} {rivers_}")    

print("==============================================")
print("")
print("Exercise 6-6 Polling ")

should_take = {
    'Thais',
    'Gabriel',
    'Rose',
    'Paulo',
    'Sergey',
    'Alyssa',
    'Henri',
}

have_taken = {
    'Thais',
    'Gabriel',
    'Rose',
    'Paulo',
    'Marcelo',
    'Lucas',
    'Geraldo',
}

for key in should_take:
    if key in have_taken:
        print(f"Thank you for taking the poll {key}")
    else:
        print(f"Please, take the poll {key}")

