
from functools import reduce

def max(set):
    m= reduce(lambda x,y: x if x>y else y ,s11)
    return m

s1={2,4,1,3,8,9,6,5}
s11 = s1
m=max(s11)
s1.remove(m)    
print(s1) 



# s1={4,1,3,6,9,8}
# max=0
# for i in s1:
#     if i > max:
#         max=i
  
# print("the orignal set is : ", s1 )
# s1.remove(max) 
# print("the set after removing max value element is : " ,s1)     

