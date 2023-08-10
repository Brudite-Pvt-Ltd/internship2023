#Create a function that takes a list and returns a new list with unique elements of the first list.
list = [1,2,2,3,4,4,5,5]
unique_ele = []
for element in list :
    if element not in unique_ele :
        unique_ele.append(element)
print(unique_ele)