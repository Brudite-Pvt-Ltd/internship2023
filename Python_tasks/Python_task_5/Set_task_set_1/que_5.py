# program 5 : creating a set of all possible sub_sets

# creating a new set 
s = {1, 2, 3}

power_set = set()

# method 1 : brute force using recursion.

temp_set_list = list(s)


def get_power_set(i, l, sub_set, power_set):
    
    # if we reached to end then, add the sub_set we created and return;
    if i == len(l):
        power_set.add(tuple(sub_set))
        return 

    # not pick 
    get_power_set(i+1, l, sub_set, power_set)    
 
    # pick
    sub_set.append(l[i])
    get_power_set(i+1, l, sub_set, power_set)
    sub_set.remove(l[i])
    


get_power_set(0, temp_set_list, [], power_set)
print("Using Brute force : ", power_set)  



# method 2 : using bit manipulation 

power_set.clear()

# getting the length of set
n = len(temp_set_list)

for i in range((1<<n)):
    sub_set = []
    for j in range(n):
        if i & (1<<j):
            sub_set.append(temp_set_list[j])
            
    power_set.add(tuple(sub_set))


print("using bit Manipulation : ", power_set)