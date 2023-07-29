class Cars:
    def __init__(self, name, color) -> None:
     self.name = name
     self.color = color


    def print_self(self):
        print(self)
        print(self.name)
        print(self.color)
        print('/n')

class Bmw(Cars):
   def print_hello():
      print('hello')
      obj2=Bmw()
      obj2.print_self()

class Ankita(Bmw):
    def print_name():
         print('Ankita')
         obj1=Ankita()
         obj1.print_self()

        
bmw = Cars('bmw','black')
bmw.print_self()

obj2 = Cars('hundai','white')
obj2.print_self()

obj1 = Cars('audi','red')
obj1.print_self()

o =Ankita("od","blue")
o.print_self()





