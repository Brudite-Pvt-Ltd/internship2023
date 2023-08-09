# -*- coding: utf-8 -*-
"""
que5
You are developing a program that analyzes weather data. Write a Python function that takes a list of temperature readings for a specific location and determines the average temperature, highest temperature, and lowest temperature.
Input
temperature_readings = [25, 28, 21, 24, 27]
Output:
Average Temperature: 25.0
Highest Temperature: 28
Lowest Temperature: 21
"""

temperature_readings = [25, 28, 21, 24, 27]

from functools import reduce
print("Average_readings",(reduce(lambda x,y:x+y,temperature_readings)/len(temperature_readings)))
print("Highest Temprature : ",max(temperature_readings))
print("Lowest Temprature : ",min(temperature_readings))
