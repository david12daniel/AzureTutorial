import geometry as geometry

class Rectangle(geometry.Geometry):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        super().__init__()
        
    def print(self):
        print(f'Geometry ID {geometry.Geometry.id} is rectangle with length of {self.length} and width of {self.width}')
    
    def area(self):
        return self.length*self.width

    def perimeter(self):
        return self.length*2+self.width*2



    
