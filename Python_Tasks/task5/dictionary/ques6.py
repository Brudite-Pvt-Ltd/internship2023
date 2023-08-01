details = [
        {"name": "virat", "age": 34},
        {"name": "abd", "age": 38},
        {"name": "gayle", "age": 43},
        {"name": "siraj", "age": 29}        
        
    ]
d2=sorted(details,key=lambda details:details["age"])
print("orignal dictionary is : ",details)
print("sorted dictionary is : ",d2)