class Farm:

    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, count=1):
        self.animals.update({animal: count}) 

    def get_info(self):
        name_str = f"{self.name}'s Farm"
        return f"{name_str}\n {self.animals}\n E-I-E-I-0!"
    
    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        animals_list = list(self.animals.keys())
        return f"{self.name}’s farm has {', '.join(animals_list[:-1])} , and {animals_list[-1]}"
      

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())