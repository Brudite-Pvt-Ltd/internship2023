marks=[]
max_marks=[]
subject=["Physics", "Chemistry", "Mathematics", "Biology", "Computer"]
for i in range(5):
    print(subject[i])
    max_mark=int(input("Maximum marks: "))
    mark=float(input("Marks obtained: "))
    print("\n")
    max_marks.append(max_mark)
    marks.append(mark)

per = (sum(marks)/sum(max_marks))*100

if(per>=90):print("Grade A")
elif(90>per>=80):print("Grade B")
elif(80>per>=70):print("Grade C")
elif(70>per>=60):print("Grade D")
elif(50>per>=40):print("Grade E")
else:print("Grade F")

