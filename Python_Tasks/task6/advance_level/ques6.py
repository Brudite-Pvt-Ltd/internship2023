class Main():
    def __init__(self):
        pass
    def a(self):
        print("this is main class")
        
class First(Main):
    def b(self):
           print("this is second class")
           
class Second(First):
    def c(self):
        print("this is third class")  
class Third():
    def d(self):
        print("this is last class") 
class Fourth(Second,Third):
    def f(self):
        print("this is final class")        
        


obj=Fourth()
obj.a()
obj.b()
obj.c()        
obj.d()   
obj.f()     
        