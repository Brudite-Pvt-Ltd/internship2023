# Find the median of a list without using the built-in median function.

def median(list):
   
    list.sort()
    if len(list) % 2 == 1:
          return list[len(list) // 2]
    else:
         return (list[len(list) // 2 - 1] + list[len(list) // 2]) / 2
      
    
list = [1,2,23,4,5,6,7,9]
print(median(list))