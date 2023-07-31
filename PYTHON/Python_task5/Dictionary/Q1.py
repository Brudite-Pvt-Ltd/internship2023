# Create a dictionary of students and their scores,find and print the student with the highest score.

def highest_score(dict):
    highest_score = 0
    highest_score_student = ""
    for i in dict:
        if dict[i] > highest_score:
            highest_score = dict[i]
            highest_score_student = i
    return highest_score_student

dict = {"student1" : 70, "student2" : 77, "student3" : 80}
print(highest_score(dict))