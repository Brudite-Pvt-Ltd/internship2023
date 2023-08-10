#5. You are developing a program that analyzes weather data. Write a Python function that takes a list of temperature readings for a specific location and determines the average temperature, highest temperature, and lowest temperature.
# Input
# temperature_readings = [25, 28, 21, 24, 27]
# Output:
# Average Temperature: 25.0
# Highest Temperature: 28
# Lowest Temperature: 21

def temp(temperature_readings):
    n=len(temperature_readings)
    temperature_readings.sort()
    print("average_temp",sum(temperature_readings)/n)
    print("highest_temp=",temperature_readings[-1])
    print("lowest_temp=",temperature_readings[0])
temperature_readings = [25, 28, 21, 24, 27]
temp(temperature_readings)