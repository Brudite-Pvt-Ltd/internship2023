'''You are developing a program that analyzes weather data. Write a Python function that takes a list of temperature readings for a specific location and determines the average temperature, highest temperature, and lowest temperature.
Input
temperature_readings = [25, 28, 21, 24, 27]
Output:
Average Temperature: 25.0
Highest Temperature: 28
Lowest Temperature: 21
'''

def get_temperature(locations) :
    temperature = []
    for location in locations :
        temperature = get_temperature(location)
        temperature.append(temperature)
        average_temperature = sum(temperature) / len(temperature)
        highest_temperature = max(temperature)
        lowest_temperature = min(temperature)
        return average_temperature , highest_temperature, lowest_temperature
