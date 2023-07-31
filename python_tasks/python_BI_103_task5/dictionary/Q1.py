student={'nav': 80,'laksh': 78,'harsh':82,'man':89}
highest_score=0
highest_score_stu=None
for x,y in student.items():
    if y > highest_score:
        highest_score=y
        highest_score_stu=x
print("the highest scoring student",highest_score_stu)