import random
from xp import Dog

# Exercise 3 : Dogs Domesticated
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained
     
    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        print(f"{''.join([dog.name for dog in args])} all play together")

    def do_a_trick(self):
        tricks = [
            f"{self.name} does a barrel roll.",
            f"{self.name} stands on his back legs.",
            f"{self.name} shakes your hand.",
            f"{self.name} plays dead."
        ]
        if self.trained:
            return random.choice(tricks)
