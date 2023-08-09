class Time:
  def __init__(self, hours, minutes):
    self.hours = hours
    self.minutes = minutes

  def add_time(self, other_time):
    total_hours = self.hours + other_time.hours
    total_minutes = self.minutes + other_time.minutes

    while(total_minutes>=60):
        if total_minutes >= 60:
            total_hours += 1
            total_minutes -= 60

    return Time(total_hours, total_minutes)

  def display_time(self):
    print("{} hours and {} minutes".format(self.hours, self.minutes))

  def display_minute(self):
    return self.hours * 60 + self.minutes


time1 = Time(2, 50)
time2 = Time(1, 20)

added_time = time1.add_time(time2)

added_time.display_time()
print("Total minutes: {}".format(added_time.display_minute()))

        
        
        