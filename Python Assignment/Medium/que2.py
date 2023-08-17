user_list=[]
while True:
    val = input("Element:  ")
    if val.lower() in ['q', 'Q']:
        break
    user_list.append(int(val))

def remove_duplicacy(a):
    a=list(set(a))
    print(f'List after removing duplicate element {a}')

remove_duplicacy(user_list)