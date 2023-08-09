'''Aditi has used a text editing software to type some text. After saving the article as WORDS.TXT, she realised that she had wrongly typed the alphabet “J" in place of alphabet “I" everywhere in the article.
Write a function definition for JTOI() in Python that would display the corrected version of the entire content of the file WORDS.TXT with all the alphabet "J" to be displayed as an alphabet "I" on screen.
Note: Assuming that WORD.TXT does not contain any J alphabet otherwise.'''
def JTOI(file_name):
  with open(file_name, "r") as f:
    data = f.read()
    data = data.replace("J", "I")
  return data

data1 = JTOI("word.txt")
print(data1)
