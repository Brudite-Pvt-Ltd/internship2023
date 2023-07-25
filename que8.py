# 8. Given an array of integers, move all the zero elements to the end while maintaining the order of other elements.

list =[1,9,0,3,0,3,40,0,6,0,3,4]

non_zero_eleindex =0
for i in range(len(list)):
       if list[i] != 0:
           list[non_zero_eleindex] = list[i]
           non_zero_eleindex += 1
    
for i in range(non_zero_eleindex, len(list)):
    list[i] = 0
print(list)