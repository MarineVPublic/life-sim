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