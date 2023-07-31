# 3.Find the frequency of each element in a list and store it in a dictionary.
list = [1, 2, 4, 2, 3, 5, 4, 3, 6, 5, 7, 2, 3, 4]
dict = {}
for i in list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print("frequency of each element :", dict)