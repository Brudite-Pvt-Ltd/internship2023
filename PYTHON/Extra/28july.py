class Cars:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
    def print_self(self):
        print(self)
        print(self.name)
        print(self.color)

class Gaadi(Cars):
    def naam(self):
        print(self.name)

class Pahiya(Gaadi):
    def print_wheel(self):
        print(self.color)

class Chauthi(Gaadi,Cars):
    def chauthi(self):
        print(self.name)

obj1 = Cars('bmw','black')
obj1.print_self()
obj2 = Cars('audi','silver')
obj2.print_self()
obj3 = Cars('porche','gold')
obj3.print_self()
obj4 = Gaadi('hyundai','white')
obj4.naam()
obj5 = Pahiya('alto','brown')
obj5.print_wheel()
obj6 = Chauthi('Swift','black')
obj6.chauthi()
obj6.naam()