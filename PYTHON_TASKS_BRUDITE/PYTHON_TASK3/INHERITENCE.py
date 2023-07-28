class Cars:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color= color
    def my_func (self):
        print(self.name)
obj1= Cars("Yellow","BMW")
obj1.my_func()    
class Model(Cars):
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
    def my_func1(self):
        print(self.color)
obj2=Model("NISSAN", "GREEN")
obj2.my_func1()
class Age(Model):
    def my_fun2():
        pass
obj3  = Age("hello","blue")
obj3.print_hello()
        
    
            
