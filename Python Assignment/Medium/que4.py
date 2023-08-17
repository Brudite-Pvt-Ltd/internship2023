user_list = []
while True:
    val = input("Element:  ")
    if val.lower() in ['q', 'Q']:
        break
    user_list.append(int(val))
d = int(input("Enter vlaue for D:  "))
user_list=user_list[::-1]
ele=[]
print(user_list)
for i in range(d):
    ele.append(user_list[i])
user_list=user_list[::-1]
for i in range(d):
    user_list.pop()
for i in range(len(ele)):
    user_list.insert(0,ele[i])
print(user_list)