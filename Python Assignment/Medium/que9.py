user_list=[1,2,3,4,5]
print(f'Given list is: {user_list}')
print(f'Length of the list is: {len(user_list)}')
print('Looping over the list to make Index error')
try:
    for i in range(len(user_list)+1):
        print(user_list[i])
except IndexError:
    print("Hurry!! We encountered Index Error")

