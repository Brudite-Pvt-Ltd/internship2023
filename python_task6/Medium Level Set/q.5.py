# You are developing a program that analyzes weather data. Write a Python function that takes a list of temperature readings for a specific location and determines the average temperature, highest temperature, and lowest temperature.
# Input
# temperature_readings = [25, 28, 21, 24, 27]
# Output:
# Average Temperature: 25.0
# Highest Temperature: 28
# Lowest Temperature: 21

list_temp = [25, 28, 21 ,24 ,27]
list_temp.sort()
print(list_temp)
print("average temprature:"+str(list_temp[len(list_temp)//2]))
print("Higest temprature : "+str(list_temp[4]))
print("Lowest temprature : "+str( list_temp[0]))
