class Shape :
    def __init__(self):
        pass
    
    def area(self):
        print("Shape area : 0")
        
        
class Square(Shape):
    def __init__(self, l):
        self.l = l
        
    def area(self):
        print("Square area : ", self.l*self.l)


Shape_obj = Shape();
Shape_obj.area();


Square_obj = Square(5)
Square_obj.area();
