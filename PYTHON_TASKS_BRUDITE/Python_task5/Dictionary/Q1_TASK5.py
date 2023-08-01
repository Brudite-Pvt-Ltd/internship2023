# Create a dictionary of students and their scores,find and print the student with the highest score.

student={'chris': 90,'jack': 25,'bob':55,'harry':49}
highest_score=0
highest_score_stu=None
for x,y in student.items():
    if y > highest_score:
        highest_score=y
        highest_score_stu=x
print("the highest scoring student",highest_score_stu)