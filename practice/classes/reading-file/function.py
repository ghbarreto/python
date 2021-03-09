import user

def split(f):
    
    for x  in f:
        for y in x:
            name = y.split(',')[0]
            last_name = y.split(',')[1]
            age = y.split(',')[2]
            nationality = y.split(',')[3]
            
            right_name = name.strip("''")
            right_last_name = last_name.strip("''")
            right_age = age.strip("''")
            right_nationality = nationality.strip("''")
            
            name = user.Read(right_name, right_last_name, right_age, right_nationality)
            name.writef()
            name.read()