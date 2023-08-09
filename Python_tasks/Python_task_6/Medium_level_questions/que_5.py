# program 5 :
    
temperature_readings = [25, 28, 21, 24, 27]

mx = -1e9
mn = 1e9
avg = 0

for x in temperature_readings:
    avg += x
    mx = max(mx, x)
    mn = min(mn, x)
    
print("Average Temperature : ", avg/len(temperature_readings))
print("Highest Temperature : ", mx)
print("Lowest Temperature : ", mn)