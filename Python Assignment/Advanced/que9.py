user_string = "wwwwaaadebbbbbw"
user_string_list=[]

for letter in user_string:
    user_string_list.append(letter)
print(user_string_list)

new_user_string_list=[]    

for i in range(len(user_string_list)-1):
    letter_list = []
    
    current_letter = user_string_list[i]
    next_letter = user_string_list[i+1]

    if next_letter == current_letter:
        letter_list=[]
    else:
        letter_list.append(next_letter)
        

    new_user_string_list.append(letter_list)


