student={'nav': 80,'laksh': 78,'harsh':82,'man':89}
old_key='harsh'
new_key='harshita'
if old_key in student:
    student[new_key]=student.pop(old_key)
    print("modified dict:-",student)