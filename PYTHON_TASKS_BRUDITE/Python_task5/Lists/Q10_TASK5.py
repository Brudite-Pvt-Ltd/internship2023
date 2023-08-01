# Q10. Write a function that takes a list of integers as input
# and rearranges the elements so that all negative elements appear before the non-negative elements,
# and the order of elements within each category remains unchanged.
# The goal is to do this in-place,i.e.,without using any additional data structures.
# For example, given the list:[3,-1,-4,2,0,-5,6,-2], after rearranging,
# the output should be: [-1,-4,-5,-2,3,2,0,6].

def re_arrange(list):
    left_ptr = 0  

    for right_ptr in range(len(list)):
        if list[right_ptr] < 0:
            for i in range(right_ptr, left_ptr, -1):
                list[i], list[i-1] = list[i-1], list[i]
            left_ptr += 1
    return list

l1 = [3,-1,-4,2,0,-5,6,-2]
print(re_arrange(l1))
