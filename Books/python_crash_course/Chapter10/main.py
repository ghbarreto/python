filename = 'texts/text1.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print("===================================")

million = 'texts/million_text.txt'

with open (million) as file_object:
    linez = file_object.readlines()

string = ''

for lineM in linez:
    string += lineM.strip()

# birthday = input("Enter your birthday, in the form ddmmyy:")

# if birthday in string:
#     print("Your birthday appears in the first million digits of pi")
# else:
#     print("im sorry")

print(f"{string[:10]}...")
print(len(string))

print("===========================================")

file = 'texts/learning_python.txt'

with open(file) as files:
    z = files.readlines()

for lines in z:
    for i in range(0,3):
        print(lines.rstrip()) 

print("===========================================")

message = "a"

with open (file) as test:
    x = test.readlines()
for y in x:
    print(y.replace("python", "java").rstrip())