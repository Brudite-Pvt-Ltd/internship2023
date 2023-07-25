set1 = {33, 22, 44}                  #1
set2 = {22, 33, 55}
difference = set1.difference(set2)
print(difference)   


symmetric_difference = set1.symmetric_difference(set2)    #2
print(symmetric_difference)               

set3 ={11,22,33,44,55,66,77}          #3
result = set1.issubset(set3)
print(result) 

result = set1.isdisjoint(set2)
print(result)                         #4


removed = set3.pop()
print(removed)                       #5 
print(set3) 