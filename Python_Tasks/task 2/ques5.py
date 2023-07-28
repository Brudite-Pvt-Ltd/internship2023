list = [3, 6, 9, 12, 15]
a=1
for i in range(1, len(list)):
    if (list[i] <= list[i-1]):
        a=0
        
if(a==0):
   print("no , this list is not increasing strictly") 
else:
   print("yes , this list is increasing strictly") 
        
                   
            