# Write a Python function to check if an element exists in an array.

ank_array = [1,2,3,4,5]
element = int(input("enter value"))
print(element)
for item in ank_array:
    if item == element:
        print("element is present in ank_array")
    else:
        print("element is not present in ank_array")
