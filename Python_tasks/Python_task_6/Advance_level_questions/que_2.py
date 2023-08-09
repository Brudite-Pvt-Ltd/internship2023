# program 2 :
    
import os

file = open(os.path.dirname(__file__) + "\doc.txt")

ln = len(file.read().split('\n'))
print(ln)