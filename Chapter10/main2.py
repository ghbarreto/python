filename = 'write/file.txt'

with open(filename, 'w') as file_object:
    for i in range(0, 2):
        file_object.write(f"{i}.\n")

with open(filename, 'a') as appending:
    appending.write("I love you\n")
    appending.write("You love me too.")

with open(filename) as fileRead:
    file = fileRead.readlines()
    for txt in file:
        print(txt.rstrip())

print("==============================================")

name = input("What is your name:")
print("-----------")
gest = 'write/guest.txt'


with open(gest, 'a') as guest:
    guest.write(f"{name}, \n")

with open(gest) as readGuest:
    value = readGuest.readlines()
    for val in value:
        print(val.rstrip())

print("==============================================")

guest_book = 'write/guest_book.txt'
loop = True
all_names = []

while loop:
    name2 = input("What is your name: ")

    if name2 == 'q':
        loop = False
    else:
        print(f"Hello {name2}, thank you for coming.\n")
        with open(guest_book, 'a') as guestb:
            guestb.write(f"Hello {name2}, thank you for coming.\n")

with open(guest_book) as read_guestbook:
    zx = read_guestbook.readlines()
    for zz in zx:
        print(zz.rstrip())

print(all_names)

print("==============================================")

programming = 'write/file_programming.txt'

pollT = True

while pollT:
    question = input("why do you like programming: ")

    if question == 'q':
        pollT = False
    else:
        with open(programming, 'a') as poll:
            poll.write(f"The reason why i like programming is {question}. \n")

with open(programming) as read_poll:
    r = read_poll.readlines()
    for rx in r:
        print(rx.rstrip())



