from abstract  import shape
class Rectangle(shape):
    def __init__(self):
        self.length=6
        self.breadth=8
    def area(self):
        return (self.length*self.breadth)
r=Rectangle()
print(r.area())
r.display