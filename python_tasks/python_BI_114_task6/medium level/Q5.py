def temp(temp_read):
    n=len(temp_read)
    temp_read.sort()
    print("average_temp",sum(temp_read)/n)
    print("highest_temp=",temp_read[-1])
    print("lowest_temp=",temp_read[0])
temperature_readings = [25, 28, 21, 24, 27]
temp(temperature_readings)