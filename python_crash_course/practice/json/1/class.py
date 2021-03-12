import main

def input_name():
    ''' Input the name to be found in the query '''
    request = True
    name_arr = []

    while request: 
        name = input("Display All: A\nExit: Q\nCountry Name: c\nChoose a name: ")
        

        if name == 'q':
            print("Bye bye.")
            request = False
            main.choose_name(name_arr)
        elif name == 'a':
            main.display_all("")
            request = False
        elif name == 'c':
            input_country()
            request = False
        else:
            name_arr.append(name) 

def input_country():
    country = input("Country name is: ")
    main.display_country(country)

# main.display_country("")
input_name()