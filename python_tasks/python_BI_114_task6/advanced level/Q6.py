'''Create the custom python classes which has methods and attributes and implement single inheritance, multiple inheritance and multilevel inheritance'''
class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def print1(self):
        print("name of the student:-",self.name)
        print("roll_id of the student:-",self.id)   
        
class Marks1(Student):
    def __init__(self, name, id,maths,physics,cs):
        super().__init__(name, id)
        self.maths=maths
        self.physics=physics
        self.cs=cs
        
    def total_marks(self):
        sum=self.maths+self.physics+self.cs
        print("total marks:-",sum)
        return sum
        
class Marks2(Student):
    def __init__(self, name, id,maths,physics,cs):
        super().__init__(name, id)
        self.maths=maths
        self.physics=physics
        
        self.cs=cs
        
    def total_marks(self):
        sum=self.maths+self.physics+self.cs
        print("total marks:-",sum)
        return sum
                
class Percentage(Marks1):
    
        
    def percent(self,sum):
        per=(sum//3)*100
        print("percentage :-",per)
   
#class  Check(Perantage,Marks2):
   # def   
obj1=Student("Nav","01")
a=int(input("enter the marks of maths"))
b=int(input("enter the marks of physics"))
c=int(input("enter the marks of cs"))
obj2=Marks1("nav","01",a,b,c)
obj2.print1()
total_marks1=obj2.total_marks()
obj3=Percentage()
obj3.percent(total_marks1)

           
          
    
         
        



