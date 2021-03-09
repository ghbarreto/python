txt = 'text.txt'

class Read:
    
    def __init__(self, name, last_name, age, nationality):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        
    def writef(self):
        with open(txt, 'a') as append_file:
            append_file.write(f"name: {self.name}\nlast name: {self.last_name}\nage: {self.age}\nnationality: {self.nationality}\n---------------------- \n")
    
    def read(self):
        with open(txt) as read_file:
            r = read_file.readlines()
            for i in r:
                print(i.rstrip()) 

    def erase(self):
        with open(txt, 'w') as erase_file:
            erase_file.write('')