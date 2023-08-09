"""que7
Write a program to construct a dictionary from the two lists containing the names of students and
their corresponding subjects. The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension.
"""

studentlist = ['manoj','raghav','jay','veeru','harish','vikash']
subjectlist = ['maths','Arts','commerce','computer','Science' ,'Biology']

dictionary = {x:y for x,y in zip(studentlist,subjectlist)}
print(dictionary)