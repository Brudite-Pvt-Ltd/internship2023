# Q1.Create a set with elements from 1 to 10. Check if it is a subset of {0,5,10,15}.

s1 = set(range(1,11))
print(s1)
s2= {0,5,10,15}
def check(s1,s2):
 for i in s1:
    if i not in s2:
       return False
 return True
print(check(s1,s2))