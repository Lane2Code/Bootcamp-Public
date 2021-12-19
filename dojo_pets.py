class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self): # walk() - walks the ninja's pet invoking the pet play() method
        self.pet.play()
        return self
        
    def feed(self): # feed() - feeds the ninja's pet invoking the pet eat() method
        pass
    def bathe(self): # bathe() - cleans the ninja's pet invoking the pet noise() method
        pass

david = Ninja("David", "L.", "BilJac", "GatsroFun", "dog")
lisa = Ninja("Lisa", "A.", "CatNibbles", "CannedFood", "cat")

class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
        self.noise = noise

    def sleep(self, energy): # sleep() - increases the pets energy by 25
        self.energy += 24
        return self
        
    def eat(self, energy, health): # eat() - increases the pet's energy by 5 & health by 10
        self.energy += 5
        self.health += 10
        return self

    def play(self, health): # play() - increases the pet's health by 5
        self.health += 5
        return self

    def noise(self): # noise() - prints out the pet's sound
        print(self.noise)

rhea = Pet("Rhea","German Shepard", "many", "ruff ruff grrrr")
summer = Pet("Summer", "house cat", "scratching", "meow meooooow")