class Shape:
    def __init__(self):
        self.area=0
    def area(self):
        return self.area
         
class Square(Shape):
    def _init__(self,length):
        super().__init__()
        self.length=length
    def area(self):
            area=self.length*self.length
            print("area of the shape whose lenght is {} is {}".format(self.length,area))
obj=Square(4)
obj.area()
