"""
que3
Aditi has used a text editing software to type some text. After saving the article as WORDS.TXT, she realized that she had wrongly typed the alphabet “J" in place of alphabet “I" everywhere in the article.
Write a function definition for JTOI() in Python that would display the corrected version of the entire content of the file WORDS.TXT with all the alphabet "J" to be displayed as an alphabet "I" on screen.
Note: Assuming that WORD.TXT does not contain any J alphabet otherwise.
"""

def JTOI(content):
    return [x.replace("J","I") for x in content]

file_name = input("enter file name with its prefferd extensions in which u want to perform JTOI:")
with open(file_name,'r') as file:
    t = JTOI(file.readlines())
with open(file_name,'w') as file:
    for x in t:
        file.write(x +"\n")
    

