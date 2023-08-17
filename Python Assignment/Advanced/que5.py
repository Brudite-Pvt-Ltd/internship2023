import datetime
class Time():
    def __init__(self, time_obj1, time_obj2, time_obj):
        self.addTime(time_obj1, time_obj2)
        self.displayTime()
        self.displayMinute(time_obj)

    def addTime(self, time_obj1, time_obj2):
        minute = time_obj1[1]+time_obj2[1]
        hour = time_obj1[0]+time_obj2[0]
        if minute >=60:
            a = minute-60
            minute=a 
            hour+=1
        print(f'Total hours: {hour} and Total minutes: {minute}')
    
    def displayTime(self):
        print(f'{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}')
    
    def displayMinute(self, time_obj):
        print(f'Total minutes: {time_obj[0]*60+time_obj[1]}')
    

my_time = Time([2, 50], [1, 20], [1, 2])