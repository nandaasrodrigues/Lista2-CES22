from abc import abstractmethod
import math

class Meal(object):
    def __init__(self, radius, height, ingredients):
        self.plate_radius = radius
        self.plate_height = height
        self.ingredients = ingredients

    @staticmethod
    def mix_ingredients(ingredients):
        food = ''
        for i in ingredients:
            food = food + i + ' '
        return food

    def cook(self):
        print('Let\'s cook ' + self.mix_ingredients(self.ingredients))

    @staticmethod
    def compute_area(radius):
         return math.pi * (radius ** 2)

    @classmethod
    def compute_volume(cls, height, radius):
         return height * cls.compute_area(radius)

    def get_volume(self):
        return self.compute_volume(self.plate_height, self.plate_radius)

    @classmethod
    def get_radius(cls):
        return cls.plate_radius
    
    @abstractmethod
    def time(self):
         """Method that should do something."""
         pass
    
    

meal = Meal(10, 3, ['rice', 'beans', 'potato'])
meal.cook()
meal.get_volume()