user_str=str(input("Enter your encrypted string: "))
user_str = user_str.split("0")
input_list=['First Name', 'Last Name', 'id']
user_str = [x for x in user_str if x!='']
user_dict={x:y for (x,y) in zip(input_list, user_str) }
print(user_dict)