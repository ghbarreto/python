import main

def input_name():
    ''' Input the name to be found in the query '''
    request = True
    name_arr = []

    while request: 
        name = input("Choose a name: ")

        if name == 'q':
            request = False
            main.choose_name(name_arr)
        else:
            name_arr.append(name) 

input_name()