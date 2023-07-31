#Q1.WAP to count all unique values in the list.
#method 1.
ank=[1,2,3,5,23,45,23,34,56,45,56,23,7,8]
unique_values=set(ank)
print(unique_values)
c= len(set(ank))
print(c)

#method 2.
list2 = [2,4,5,6,7,3,4,67,45,56,67,34,56,2,4,9,0]
l1=[]
count=0
for item in list2:
    if item not in l1:
        count+=1
        l1.append(item)


print("the number of item are",count)

#method 3.
dict={'ankita':[ 3,4,5,7,6,6,8]}
print(dict)
unique_items = list({ele for val in dict.values() for ele in val})
count = len(unique_items)
print(count)



    

