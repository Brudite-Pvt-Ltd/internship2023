"""
que6
Create the custom python classes which has methods and attributes and implement single inheritance, 
multiple inheritance and multilevel inheritance
"""
#Vehicle type represent a vehicle may be car ,bike,truck anything 
class vehicle:
    def __init__(self,type) -> None:
        self.type = type
    
    def v_type(self):
        return self.type
    
    def display_V_type(self):
        print(f'Vechile is {self.type}')

class color:
    def __init__(self, name):
        self.name = name
    def colors(self):
        return self.name
    
#single inheritance 
class Engine(vehicle):
    def __init__(self,type, fuel_type):
        super().__init__(type)
        self.fuel_type = fuel_type
    def Engine_type(self):
        return self.fuel_type
    def v_engine_type(self):
        return [super().v_type(),self.fuel_type]

#multilevel inheritence
class Car(Engine):
    def __init__(self, type,fuel_type,name):
        super().__init__(type,fuel_type)
        self.name = name
    def c_name(self):
        return self.name
    def c_type_name(self):
        return [super().v_engine_type(),self.name]
# multiple inheritance
class bike(Engine):
    def __init__(self, type,fuel_type,name):
        super().__init__(type,fuel_type)
        self.name = name
    def b_name(self):
        return self.name
    def b_type_name(self):
        return [super().v_engine_type(),self.name]


#mulitple inheritance
class color_of_vechile(color,vehicle):
    def __init__(self,type,name):
        color.__init__(self,name)
        vehicle.__init__(self,type)

    def display(self):
        print(f'You {vehicle.v_type(self)} is of {color.colors(self)}')


#obj of multiple inheritace
obj1 = color_of_vechile('car','red')
obj1.display()

#mulitlevel inhertence obj
obj2 = Car('car','Petrol Engine ','Ford Mustang GT')
obj2.display_V_type()
print(f'{obj2.c_type_name()[1]} {obj2.c_type_name()[0][0]} has a {obj2.c_type_name()[0][1]}')

#single Inheritence
obj3 = Engine('car','diesel')
print(f'this {obj3.v_engine_type()[0]} has a  {obj3.v_engine_type()[1]} Engine in it')