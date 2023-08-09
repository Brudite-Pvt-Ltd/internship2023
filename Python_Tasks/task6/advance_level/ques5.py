
class Time():
    def __init__(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes
        
    def addTime(self, t1):
        hour = self.hour + t1.hour
        minutes = self.minutes + t1.minutes
        hour += minutes // 60
        minutes = minutes % 60
        return Time(hour,minutes)
        
    
    def displayTime(self):
         print(self.hour ,"hours", self.minutes, "minutes")
    
    def displayMinutes(self):
        return self.hour*60 + self.minutes
    
t1 = Time(2, 50)
t2 = Time(1, 20)

t3 = t1.addTime(t2)
t3.displayTime()
print(t3.displayMinutes(),"minutes")
    
        