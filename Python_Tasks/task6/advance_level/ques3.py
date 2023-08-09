
def JTOI(a, x, y):
    with open(a, 'r') as file:
        lines = file.readlines()
    
    st= [i.replace(x, y) for i in lines]
     
    with open(a, 'w') as file:
        file.writelines(st)
        


a = "V:\WORDS.txt"   # Path name
print("Original file content:")
print("")
with open(a, 'r') as file:
    for i in file:
        print(i, end="")
print("")

x = input("Enter the incorrect word: ")
y = input("Enter the correct word: ")
new = JTOI(a, x, y)
print("The file after replacement is:")
print("")
with open(a, 'r') as file:
    for i in file:
        print(i, end="")













     
     

 