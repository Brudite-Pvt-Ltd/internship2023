""""
que4
Define a class named Shape and its subclass Square. The Square class has an init
function which takes length as argument. Both classes have an area 
function which can print the area of the shape where Shape’s area is 0 by default.
"""

class Shape:
    def __init__(self,length = 0) -> None:
        self.length = length

    def area(self):
         print("area of a Shape:",self.length**2)
class Square(Shape):
    def __init__(self, length=0) -> None:
        super().__init__(length)
        self.length = length
    
    def area(self):
        print("area of a square : ",self.length**2)

obj1 = Shape(5)
obj1.area()
obj2 = Square()
obj2.area()
