# Exercise 1: Cats
# Instructions
#     Instantiate three Cat objects. Outside of the class, create a function that finds the oldest cat and returns the cat.

#     Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.


class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def find_oldest(pet_list):
    oldest_age = pet_list[0].age
    result = pet_list[0]
    for pet in pet_list:
        if pet.age > oldest_age:
            result = pet 
    return result

cat1 = Cat("Abe", 1)
cat2 = Cat("Benny", 2)
cat3 = Cat("Casie", 3)
oldest_cat = find_oldest([cat1, cat2, cat3])
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old")


# Exercise 2 : Dogs
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high!")

def get_bigger(pet1, pet2):
    if pet1.height > pet2.height:
        print(f"{pet1.name} is bigger")
    else:
        print(f"{pet2.name} is bigger")

davids_dog = Dog("Rex", 50)
print(davids_dog.__dict__)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(sarahs_dog.__dict__)
sarahs_dog.bark()
sarahs_dog.jump()

get_bigger(davids_dog, sarahs_dog)

# Exercise 3 : Who’s the song producer?
# Define a class called Song, it will show the lyrics of a song.
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo

class Zoo: 
    def __init__(self, zoo_name) -> None:
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)
    
    def sell_animal(self, animal_sold):
        self.animals.remove(animal_sold)
    
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        result = {}
        key=1
        result[key] = sorted_animals[0]
        for i in range(1, len(sorted_animals)):
            if sorted_animals[i][0] != sorted_animals[i-1][0]:
                key += 1
            result.update({key: sorted_animals[i]})
        return result

    def get_groups(self):
        print(self.sort_animals())

ramat_gan_safari = Zoo("Ramat Gan Zoo")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Zebra")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Lion")
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups()
ramat_gan_safari.sort_animals

