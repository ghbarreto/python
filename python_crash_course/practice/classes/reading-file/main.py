import user
from function import split

request = True
lists = []
end = []
usr = 0

while request:
    start = input('to quit press Q: ')
    delete = input('to delete file press L: ')

    if start == 'q':
        request = False
        break 
    elif delete == 'l':
        request == False
        user.Read.erase('erasing')
        break
    else:
        usr = usr + 1
        name_input = input("What is your name: ")
        last_name_input = input("What is your last name: ")
        age_input = input("What is your age: " )
        nationality_input = input("What is your nationality: ")
        end= {"'{}','{}','{}','{}'".format(name_input, last_name_input, age_input, nationality_input)}        

        lists.append(end)
        split(lists)


