class User: 

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def show(self):
        return print(f"Inside user your name is {self.name} {self.last_name}")