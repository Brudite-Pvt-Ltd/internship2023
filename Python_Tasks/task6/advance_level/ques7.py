students = ["Naresh", "Suresh", "Mukesh"]
subjects = ["Math", "physics", "chemsitry"]
d={}
for i in range(len(students)):
    d[students[i]]=subjects[i]
print(d)

print({students[i]:subjects[i] for i in range(len(students))})
