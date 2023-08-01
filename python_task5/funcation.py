'''file = open("hello.txt.txt",'r')
print(file.read(3))
file.close()'''

try :
    file = open("hello.txt",'r')
    print(file)

except Exception as e :
  print(e)

print("done")