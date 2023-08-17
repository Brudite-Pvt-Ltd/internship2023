#Write a Python program to find the common elements between two lists.
#Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8]
  
def common_ele(l1, l2):
    l1_set = set(l1)
    l2_set = set(l2)
 
    if (l1_set & l2_set):
        print(l1_set & l2_set)
    else:
        print("No common elements")
          
  
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
common_ele(l1, l2)
  

