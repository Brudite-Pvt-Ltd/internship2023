class shape():
    def __init__(self):
        pass
class square(shape):
    def __init__(self,l=0):
        self.l=l
    def area(self):
        return self.l*self.l
    
        
obj=square(5)
print("the area of square is ", obj.area())        
        