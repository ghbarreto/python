class Person():
    pass

person = Person()

first_key = 'first'
first_val = 'Corey'
#? person_info = {'first': 'Corey', 'last': 'Schaefer'}
setattr(person, first_key, first_val)

#* setting the key and the value to the person
first = getattr(person, first_key, first_val) 
#? result: {'first': 'Corey'}

print(first)