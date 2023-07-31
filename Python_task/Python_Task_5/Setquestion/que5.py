#5. Create a set of all possible subsets from a given set

set1 ={1,2,3,4}


power_set = set()

temp_set_list = list(set1)

def get_power_set(i, l, sub_set, power_set):

    if i == len(l):
        power_set.add(tuple(sub_set))
        return 

    get_power_set(i+1, l, sub_set, power_set)    
 
    sub_set.append(l[i])
    get_power_set(i+1, l, sub_set, power_set)
    sub_set.remove(l[i])

get_power_set(0, temp_set_list, [], power_set)
print("Using Brute force : ", power_set)  
