# Exercise 1 : Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
     def sing(self, sounds):
        return f'{sounds}'

benny = Bengal("Benny", 5)
chico = Chartreux("Chico",10)
sammy = Siamese("Sammy", 20)
all_cats = [benny, chico, sammy ]

sara_pets = Pets(all_cats)
sara_pets.walk()


# Exercise 2 : Dogs
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return self.weight/self.age*10

    def fight(self, other_dog):
        winner = None
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            winner = self
        else:
            winner = other_dog
        return f"{winner.name} won the fight"


archie = Dog("Archie", 1, 10)   
bingo = Dog("Bingo", 2, 20)
cassie = Dog("Cassie", 3, 30)

print(archie.bark())
print(bingo.run_speed())
print(cassie.fight(archie))

