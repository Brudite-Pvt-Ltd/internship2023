class Car:
    def __init__(self,name,color) -> None:
        self.name=name
        self.color=color

    def print_self(self):
        print(self)
        print(self.name)
        print(self.color)
        print("/n")

        
        

bmw = Car('bmw','black')
bmw.print_self()

bmw = Car('audi','red')
bmw.print_self()

obj1=Car()
obj1.print_self()
        

class Bmw(Car):
    def print_hello():
        print('hello')
obj2=Bmw()
obj2.print_hello()

class Audi(Bmw):
 def print_hii():
        print('hii')
obj3 = Audi()
        
obj3.print_hii() 

obj3.car
class Age(Model):
