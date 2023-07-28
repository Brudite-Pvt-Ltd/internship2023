list1=[1,2,3,3,2,4]  #1method set
list2=set(list1)
print(len(list2))


list3=[]                #2 method by using loop
for i in list1:
    if i  not in list3:
        list3.append(i)
print(len(list3)) 

from collections import Counter  #3 by using counter

counter = Counter(list1)
print(len(counter.keys()))
      