# program 6 :
    
class SuperClass :
    def __init__(self):
        print("\nCreating SuperClass")
        
    def print_super_class(self):
        print("\nSuper Class")
        

class SubClass1(SuperClass):
    def print_sub_class1(self):
        print("\nSub Class 1")
        
    
class SubClass2(SuperClass):
    def print_sub_class2(self):
        print("\nSub Class 2")
        
    
class ChildClass(SubClass1, SubClass2):
    def print_child_class(self):
        print("\nChild Class")
        

obj_child = ChildClass();
obj_child.print_child_class();
obj_child.print_sub_class1()
obj_child.print_sub_class2()
obj_child.print_super_class()


