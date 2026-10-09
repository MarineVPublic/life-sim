class Colleague:
    def __init__(self, name:str, energy:int, social:int):
        self.name = name
        self.energy = energy
        self.social = social

    def display(self):
        print(f"{self.name} : level of energy: {self.energy} level of social: {self.social}")

    def decrease_needs(self):
        self.energy -= 5
        self.social -= 5
        print(f"--Needs of {self.name} have decreased--")

    def toDiscuss(self, other):
        self.energy -= 2
        self.social += 5
        other.energy -= 2
        other.social += 5
        print(f"--{self.name} discuss with {other.name}--")

    def toRest(self):
        self.energy += 15
        print(f"--{self.name} rests--")

    def __repr__(self):
        return f"Colleague({self.name}, {self.energy}, {self.social})"