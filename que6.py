#Implement a function to check if an array is a palindrome (reads the same forwards and backwards).

list =  [1,2,3,2,1]

list1 = list.copy()
list = list[: :-1]

print(list1)
print(list)

if list == list1:
    print("list is palidrome")
else:
    print("list is not a palidrome")