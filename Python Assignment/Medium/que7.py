user_list = []
while True:
    val = input("Element:  ")
    if val.lower() in ['q', 'Q']:
        break
    user_list.append(int(val))

if(len(user_list)%2==0):
    median = (user_list[int(len(user_list)/2)]+user_list[(int(len(user_list)/2))+1])/2
    print(f'Median of the giver list is {median}')
else:
    median = user_list[int(len(user_list)/2)+1]
    print(f'Median of the giver list is {median}')
