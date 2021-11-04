from pet import Pet

class Ninja:
    def __init__(self, first_name, last_name, pet_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = None
    
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

michael = Ninja("Michael", "Scott", "Chippers", "woodchips", "chicken")
michael.pet = Pet("Chippers", "beaver", "stand", "chomp chomp")

michael.walk()
michael.feed()

print(michael.pet.health)
print(michael.pet.energy)

