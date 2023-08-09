"""
que5
Create a Time class and initialize it with hours and minutes.
Create a method addTime which should take two Time objects and add them.
E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
Create another method displayTime which should print the time.
Also create a method displayMinute which should display the total minutes in the Time.
E.g.- (1 hr 2 min) should display 62 minutes

"""


class Time:
    def __init__(self,hours=0,minutes=0) -> None:
        self.hours = hours
        self.minutes = minutes
    def addtime(self,obj1):
        self.minutes = (obj1.minutes + self.minutes) % 60
        self.hours = obj1.hours + self.hours + (obj1.minutes // self.minutes)
    def display(self):
        print(self.hours,"hours ",self.minutes,"minutes")

    def displayminutes(self):
        print("(",self.hours,"hours ",self.minutes,"minutes) total in minutes ",self.hours*60 + self.minutes)
first = Time(3,56)
second = Time(5,37)
second.display()
second.displayminutes()
first.display()
first.displayminutes()
second.addtime(first)
second.display()
second.displayminutes()