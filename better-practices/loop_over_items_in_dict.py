class Person():
    pass

person = Person()

person_info = {'first': 'Corey', 'last': 'Schaefer'}
#? translating dictionary into a class
for key, value in person_info.items():
    setattr(person, key, value)
#? this loop sets the person the first key "first", and val "Corey"

#* this prints the key
for key in person_info.keys():
    print(getattr(person, key))
