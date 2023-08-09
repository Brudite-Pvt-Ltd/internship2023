# program 3 :
    
import os

f = ""
with open(os.path.dirname(__file__) + "/WORD.txt" , 'r') as file :
    f = file.read()

def JtoI(f):
    return ''.join( [ 'i' if x == 'j' else 'I' if x == 'J' else x for x in f ] ) 

new_content = JtoI(f)

with open(os.path.dirname(__file__) + '/WORD.txt' , 'w') as file :
    file.write(new_content)

print("Done")
