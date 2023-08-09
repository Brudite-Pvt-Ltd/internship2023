"""
que1
Read doc.txt file using Python File handling concept and return only the even length string from the file. Consider the content of doc.txt as given below:
Hello I am a file
Where you need to return the data string
Which is of even length
Make sure you return the content in The same link as it is present.
"""


with open("doc.txt",'r') as f:
   f=  f.read()
content =''
for x in f.split():
   if len(x)%2 == 0:
      content +=" "+ x
print(content)
with open("doc.txt",'w') as f:
   f.write(content)