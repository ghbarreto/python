class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return print(f'Welcome to {self.name}, hope you like {self.cuisine_type} food.')

    
    def open_restaurant(self):
        return print("The restaurant is open")

