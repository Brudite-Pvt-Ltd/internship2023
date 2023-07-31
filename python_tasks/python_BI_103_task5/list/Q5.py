# Split a list into evenly sized chunks.

def split_fun(list1, n):
    list2=list()
    final_list=list()

    for x in range(len(list1)):
        if x == n:
            break
        else:
            list2.append(list1[x])
            list1.pop(x)

    final_list.append(list2)
    final_list.append(list1)
    return final_list


list1= [1,2,23,4,5,6,7,9]
n = 4  
new_list = split_fun(list1, n)

print(new_list)
