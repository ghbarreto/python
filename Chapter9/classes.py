class Life:

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = int(age)


    def hello(self):
        return print(f"Hello {self.name} {self.last_name}, how are you doing today?")

    def ageComparison(self):
        if self.age < 10:
            print(f'{self.name} you are quite young')
        elif self.age > 10:
            print(f"{self.name} you are getting older")


