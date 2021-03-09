quits = input("to quit press q")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

loop = True

while loop:
    if quits == 'q':
        loop = False
        break
    else:
        try:      
            val1 = int(num1)
            val2 = int(num2)
        except ValueError:
            pass
        else:
            ans = val1 / val2
            print(ans)
            break

print("========================================")

f = ['write/dogs.txt', 'write/cats.txt', 'asdasdsad']

for filenames in f:
    try:
        with open(filenames, encoding='utf-8') as file:
            contents = file.readlines()
    except FileNotFoundError:
        print("File not found")
    else: 
        for i in contents:
            print(i.rstrip())

print("========================================")

for f2 in f:
    try:
        with open(f2, encoding='utf-8') as file:
            contents = file.readlines()
    except FileNotFoundError:
        pass
    else: 
        for i in contents:
            print(i.rstrip())

print("========================================")

file = 'write/birds_book.txt'
display = []
word = ['the']
count = 0
ans = ""

with open(file, encoding='utf-8') as bird_count:
    display = bird_count.readlines()
    for words in word:
        for d in display:
            d.split()
            if words in d:
                count = count+1
        print(f"The numbers of {words} in the book is {count}")

print("========================================")

title = []

with open(file, encoding='utf-8') as counting:
    title = counting.read()
    wording = title.split()
    num_words = len(wording)
    print(title.count('the'))
    print(num_words)

