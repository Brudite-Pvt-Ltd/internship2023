user_list=[]
while True:
    val = input("Element:  ")
    if val.lower() in ['q', 'Q']:
        break
    user_list.append(int(val))

frequency={}
for val in user_list:
    count=0
    for i in range(len(user_list)):
        if val == user_list[i]:
            count+=1
    frequency[val]=count
print(frequency)
