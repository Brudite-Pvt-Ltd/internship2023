user_list = []
print("Enter q or Q to exit")
while True:
    val = input("Element:  ")
    if val.lower() in ['q', 'Q']:
        break
    user_list.append(str(val))

new_user_list=list(map(tuple, user_list))

print(f"List after operation: \n{new_user_list}")
    