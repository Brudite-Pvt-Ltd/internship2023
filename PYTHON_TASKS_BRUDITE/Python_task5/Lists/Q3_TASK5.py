# Q3. Find the frequency of each element in a list and store it in a dictionary.

list = [4, 2, 1, 9, 4 ,3 ,7, 2, 1, 6, 8, 1, 7, 3]
dict = {}
for i in list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print("frequency of each element :", dict)