#Write a Python program to find the common elements between two lists.
'''def diff_element(l1, l2):
 return  [item for item in l1 if item  in l2]

l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
result=diff_element(l1,l2)
print("the resultant list is:", result)
'''
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
        print(l3)
