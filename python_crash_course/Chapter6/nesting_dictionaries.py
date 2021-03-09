print("==============================================")
print("")
print("Exercise 6-7 People ")

person_1 = {'name': 'Thais', 'age': 32, 'relationship': 'Married'}
person_2 = {'name': 'Gabriel', 'age': 26, 'relationship': 'Married'}

persons = [person_1, person_2]

for props in persons:
    print(props)

print("==============================================")
print("")
print("Exercise 6-8 Pets ")
# pet_5 = {'name': 'Luke', 'age': '5', 'owner:': 'Thais', 'nationality': 'Brazil'}
# pet_6 = {'name': 'Sophia', 'age': '10', 'owner:': 'Gabriel', 'nationality': 'Canada'}
# pet_7 = {'name': 'Joia', 'age': '5', 'owner:': 'Suze', 'nationality': 'Spain'}
# pet_8 = {'name': 'Nessy', 'age': '12', 'owner:': 'Liss', 'nationality': 'Belgium'}


pet_2 = {'name': 'Branca', 'owner': 'Gabriel'}
pet_3 = {'name': 'Dhara', 'owner': 'Gabriel'}
pet_4 = {'name': 'Icaro', 'owner': 'Paulo'}

pet_description = {
    'Branca' : 'A really lovely and cute cat',
    'Dhara' : 'The best friend anyone can have',
    'Icaro' : 'Beautiful bird that brightens every morning'
}

pets = [pet_2, pet_3, pet_4]

for pet in pets:
    for y, z in pet_description.items():
        if pet['name'] == y:
            print(f"{pet['name']} {z}")

print("==============================================")
print("")
print("Exercise 6-9 Favourite places ")

favourite_places = {
    'Gabriel': {
        'place': 'Vancouver',
        'country': 'Canada',
    },
    'Thais': {
        'place': 'Dublin',
        'country': 'Ireland',
    },
    'Rose': {
        'place': 'Lisbon',
        'country': 'Portugal',
    }
}

for y, key in favourite_places.items():
    print(f"{y}'s favourite place is {key['place']} that is located in {key['country']}")
        
print("==============================================")
print("")
print("Exercise 6-10 Favourite number ")

favourite_numbers = {
    'thais' : [6, 7, 8, 9],
    'gabriel' : [6, 4, 5, 10],
    'Rose': [7, 31, 4, 2],
    'Paulo': [20, 4, 9]
}

for k, y in favourite_numbers.items():
    print(f"{k}'s favourite numbers are:")
    for v in y:
        print(v)

print("==============================================")
print("")
print("Exercise 6-11 Cities")

cities = {
    'Vancouver': {
        'About': 'Vancouver is a major city in western Canada, located in the Lower Mainland region of British Columbia.',
        'Population': '2,581,000',
        'Country': 'Canada'
    },
    'Sao Paulo': {
        'About': 'The city is the capital of the surrounding state of São Paulo, the most populous and wealthiest state in Brazil.',
        'Population': '12,325,232',
        'Country': 'Brazil'
    },
    'Salvador': {
        'About': 'Founded by the Portuguese in 1549 as the first capital of Brazil, Salvador is one of the oldest colonial cities in the Americas.',
        'Population': '2.900.000',
        'Country': 'Brazil'
    }
}

for cityName, val in cities.items():
    print("")
    print(f"{cityName}")
    print(f"{val['About']}")
    print(f"{val['Population']}")
    print(f"{val['Country']}")

print("==============================================")
print("")
print("Exercise 6-12 Extensions")

cities = {
    'Vancouver': {
        'About': 'Vancouver is a major city in western Canada, located in the Lower Mainland region of British Columbia.',
        'Population': '2,581,000',
        'Country': 'Canada',
        'Pets': {
            'Cats': '200k',
            'Dogs': '500k',
            'Birds': '25m'
        },
    },
    'Sao Paulo': {
        'About': 'The city is the capital of the surrounding state of São Paulo, the most populous and wealthiest state in Brazil.',
        'Population': '12,325,232',
        'Country': 'Brazil',
        'Pets': {
            'Cats': '25m',
            'Dogs': '100m',
            'Birds': '200m'
        },
    },
    'Salvador': {
        'About': 'Founded by the Portuguese in 1549 as the first capital of Brazil, Salvador is one of the oldest colonial cities in the Americas.',
        'Population': '2.900.000',
        'Country': 'Brazil',
        'Pets': {
            'Cats': '1m',
            'Dogs': '1.5m',
            'Birds': '50m',
        },
    }
}

for v, k in cities.items():
    print(f"{v}")
    print(f"- {k['About']}")
    print(f"- Population: {k['Population']}")
    print(f"- Location: {k['Country']}")
    print(f"- Pet Population: ")
    for vs, i in k['Pets'].items():
        print(f" - {vs}: {i} ")

        


