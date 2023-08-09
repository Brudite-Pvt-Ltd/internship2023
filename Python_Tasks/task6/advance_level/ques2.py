
with open ("V:\demo.txt",'r') as file:
     text=file.readlines()
   
     for i in range(len(text)):
         i+=1
print("the number of lines in demo.txt is : ", i)         
file.close()