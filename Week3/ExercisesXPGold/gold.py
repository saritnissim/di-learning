# Exercise 1 : Geometry
import math
import random

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius
    
    def perimeter(self):
        return (2 * math.pi * self.radius)

    def area(self):
        return (math.pi * self.radius**2)

circle = Circle()
print(circle.area())
print(circle.perimeter())

# Exercise 2 : Custom List Class
class MyList:
    def __init__(self, letters):
        self.letters = letters
    
    def reverse(self):
        result = []
        for x in range(len(self.letters)-1, 0, -1):
            result.append(self.letters[x])
        return result

    def sorted(self):
        return sorted(self.letters)

    def random_list(self):
        return [random.randint() for x in range(len(self.letters))]



