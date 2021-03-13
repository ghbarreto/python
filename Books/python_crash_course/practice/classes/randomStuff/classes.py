class Human: 
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        return print (f"Hello {self.name} I see that you are {self.age} years old.")

class Races(Human):
    def __init__ (self, name, age):
        super().__init__(name, age)
        self.race = ""
        self.nationality = Nationality()

    def raceHey(self):
        return print(f"I see that you are a {self.race} person")

class Nationality:
    def __init__(self, nationality="unknown"):
        self.nationality = nationality

    def natgreet(self):
        return print(f"Inheritance is so annoying {self.nationality} ")

# human = Human("Gabriel", "25")
# human.greetings()

human = Nationality("Gabriel")
human.natgreet()