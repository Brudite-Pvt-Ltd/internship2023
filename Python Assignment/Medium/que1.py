user_list1=[]
user_list2=[]
comman_list=[]

print("Element for list 1")
while True:
    val = input("Element:  ")
    if val.lower() in ['q', 'Q']:
        break
    user_list1.append(int(val))

print("Element for list 2")
while True:
    val = input("Element:  ")
    if val.lower() in ['q', 'Q']:
        break
    user_list2.append(int(val))


for val in user_list1:
    for i in range(len(user_list2)):
        if val==user_list2[i]:
            comman_list.append(val)
comman_list=list(set(comman_list))

print(comman_list)