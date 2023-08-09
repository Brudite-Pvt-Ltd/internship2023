

with open ("V:\demo.txt",'r') as file:
     text=file.readlines()
   
     for i in range(len(text)):
         if len(text[i]) % 2 == 0:
             print(text[i],len(text[i]))
file.close()     