#Write a Python program to count the number of occurrences of a specific element in an array

list =[2,4,2,4,43,6,4,6,3,2,63,4,3,2,3,2]
ele = 2
count =0
for i in list:
    if ele == i:
        count += 1
print(list)
print(count)
#second method built in function
count = list.count(ele)
print(count)