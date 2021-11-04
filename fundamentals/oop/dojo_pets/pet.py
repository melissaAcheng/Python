class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = 10
        self.energy = 10

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        self.energy -= 5

    def noise(self):
        print(self.noise)

class Dog(Pet):
    def __init__(self, name, type, tricks, noise, age):
        super().__init__(name, type, tricks, noise)
        self.age = age

    def dog_years(self):
        self.age = int(self.age) * 7
        print(f"In dog years, {self.name} is {self.age} years old.")


border = Dog("Border", "Border Collie", "Catch", "Woof", "4")

print(border.age)
border.dog_years()