#5. Create a set of all possible subsets from a given set

set1 ={1,2,3,4}

<<<<<<< HEAD

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
=======
for i in range(len(set1)):
    tempset ={}
    for j in range(i,len(set1)):
        
    
>>>>>>> 65a2121563f275f9f600f730e4bcee05a24e56fe
