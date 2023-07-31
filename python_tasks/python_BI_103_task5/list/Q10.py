
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