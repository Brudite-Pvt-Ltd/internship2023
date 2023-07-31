#4. Check if a list is a palindrome

l1 = [1,2,3,4,2,1]
l2 =[1,2,3,4,5,4,3,2,1]

#method 1 using reverse function
if l2 == list(reversed(l2)):
    print("list is palidrome")
else:
    print("list is not a palidrome")
#method 2:
if l2 == l2[: : -1]:
    print("list is palidrome")
else:
    print("list is not a palidrome")

#method 3
for i in range(len(l2)//2):
    if l2[i]!=l2[-(i+1)]:
        print("list is not a palidrome")
    elif i == (len(l2)//2 -1):
        print("list is a palidrome")
