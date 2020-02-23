"""
@author: Anirudh Sharma
"""

class Coordiante(object):
    
    """A coordinate has two values - abscissa(x) and ordinate(y)"""
    def __init__(self, x, y):
        """Initializes x and y"""
        self.x = x
        self.y = y
    
    def __str__(self):
        """Returns the string representation of an object"""
        return "<" + self.x + ", " + self.y + ">"
    
    def distance(self, other):
        """This returns the Euclidean distance between the two coodinates"""
        x_squared = (self.x - other.x) **2
        y_squared = (self.y - other.y) **2
        return (x_squared + y_squared) ** 0.5


"""Creating objects of this class"""
p = Coordiante(3, 4)
q = Coordiante(0, 0)

print(p.distance(q))