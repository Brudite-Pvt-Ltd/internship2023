with open("demo.txt", "r") as file:
    c=0
    for line in file.readlines():
        c+=1
    print(c)