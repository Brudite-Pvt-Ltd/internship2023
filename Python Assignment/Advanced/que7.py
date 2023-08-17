student_name = ["Mohit", "Aman", "Aakash", "Vikram", "Prashant", "Rahul"]
student_subject = ["PCB", "Commerce", "PCM", "PCMB", "PCM", "Arts"]

print("\n")
print(f'Students Name list:  {student_name}')
print(f'Students Subject list:  {student_subject}')
print("\n")

# Using Dictionary Comprehension
student_data1 = {x:y for (x,y) in zip(student_name, student_subject)}
print(f'Dictionary using dictionary comprehension')
print(student_data1)
print("\n")

# Using For Loop
student_data2 = {}
for i in range(6):
    student_data2[student_name[i]] = student_subject[i]
print(f'Dictionary using for loop')
print(student_data2)
print("\n")


