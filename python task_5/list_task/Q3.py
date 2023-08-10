#Find the sum of all numeric elements in a list.
list = [1,2,3,4,5]
total = 0
for ele in range(0, len(list)) :
    total = total + list[ele]
print(total)