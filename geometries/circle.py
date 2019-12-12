import math
import geometry as geometry
class Circle(geometry.Geometry):
    def __init__(self,radius):
        self.radius=radius
        super().__init__()
        
    def print(self):
        print(f'Geometry ID {geometry.Geometry.id} is circle with radius of {self.radius}')

    def area(self):
        return math.pi*self.radius*self.radius

    def perimeter(self):
        return 2*math.pi*self.radius



