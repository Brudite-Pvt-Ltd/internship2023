#Write a Python program to find the common elements between two lists.
l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]
common_ele = []
for elements in l1 :
    if elements in l2 :
        common_ele.append(elements)
print(common_ele)