# Q2. Write a program to rename a key 

student={'chris': 90,'jack': 25,'bob':55,'harry':49}
old_key='jack'
new_key='jill'
if old_key in student:
    student[new_key]=student.pop(old_key)
    print("new dict:",student)