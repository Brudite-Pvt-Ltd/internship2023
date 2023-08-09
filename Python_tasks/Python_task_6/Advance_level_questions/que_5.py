# program 4 :
    
class Time :
    def __init__(self, hr, m):
        self.hr = hr
        self.m = m
        
    # display methods... 
    def displayTime(self):
        print("Time : ", self.hr , "hr", self.m  , "min")
        
    def displayMinute(self):
        print("Time in minutes : ", self.hr*60 + self.m , "min")
        
        
    # add time method
    def addTime(self, t):
        ht = self.hr + t.hr
        mt = self.m + t.m
        ht += mt // 60 
        mt %= 60
        new_obj = Time(ht, mt) 
        return new_obj
        
    # operator over loding 
    def __add__(self, t):
        ht = self.hr + t.hr
        mt = self.m + t.m
        ht += mt // 60 
        mt %= 60
        new_obj = Time(ht, mt) 
        return new_obj
    

# creating two objects    
t1 = Time(2, 40);
t2 = Time(1, 30);

# adding two objects and storing them into new object.

print("Using normal addTime() function to add the two objects")
t3 = Time.addTime(t1, t2)
t3.displayTime()
t3.displayMinute()

# adding the objects with operator " + "

print("\nUsing Opertor Overloding :- ")
new_obj = t1 + t2
new_obj.displayTime()
new_obj.displayMinute()