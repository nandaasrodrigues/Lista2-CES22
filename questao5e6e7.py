class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def reflect_x(self):
        return Point(self.x, -self.y)
    
    def  slope_from_origin(self):
        return self.y/self.x

    def get_line_to(self, another_point):
        m = (self.y - another_point.y)/(self.x-another_point.x)
        c = self.y - self.x*m
        return (m,c)

    def string_point(self):
        return '({},{})'.format(self.x, self.y)

print('Reflected point: ' + Point(3, 5).reflect_x().string_point())
print('Slope from origen: {}'.format(Point(4, 10).slope_from_origin()))
print('Line from origen to point: {}'.format(Point(4, 11).get_line_to(Point(6, 15))))
