class Shape:
    geometric_type = 'Generic Shape'

    def area(self): # This acts as placeholder for the interface
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

    def get_MRO(self):
        print(self.__class__.__mro__)

class Plotter:
    def plot(self, ratio, topleft):
        # Imagine some nice plotting logic here...

        print('Plotting at {}, ratio {}.'.format(topleft, ratio))

class Polygon(Shape, Plotter): # base class for polygons
    geometric_type = 'Polygon'

class RegularPolygon(Polygon): # Is-A Polygon
    geometric_type = 'Regular Polygon'
    
    def __init__(self, side):
        self.side = side


class RegularOctahedron(RegularPolygon): # Is-A RegularPolygon
    geometric_type = 'RegularOctahedron'
    
    def area(self):
        return 2 * (1 +3 ** .5)* self.side ** 2  

class RegularHexagon(RegularPolygon): # Is-A RegularPolygon
    geometric_type = 'RegularHexagon'
    
    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)

class Square(RegularPolygon): # Is-A RegularPolygon
    geometric_type = 'Square'
    
    def area(self):
        return self.side * self.side


polygon = Polygon()
print(polygon.__class__.__mro__)    

regular_polygon = RegularPolygon(5)
print(regular_polygon.__class__.__mro__)  

octahedron = RegularHexagon(10)
print(octahedron.__class__.__mro__)    

hexagon = RegularHexagon(10)
print(hexagon.__class__.__mro__)

square = Square(12)
print(square.__class__.__mro__)
