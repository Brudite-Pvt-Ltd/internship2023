list=[1,2,3,4,5,6]
n=len(list)
position=8
position=position % n 
modified_list = list[n-position:] + list[:n-position]

print("Original list:", list)
print("Rotated list:", modified_list)
