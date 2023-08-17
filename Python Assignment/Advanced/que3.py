with open("word.txt","r") as file:
    data = file.readlines()

new_data=[]

for line in data:
    a=""
    for letter in line:
        if letter == "j":
            a+="i"
        if letter == "J":
            a+="I"
        else:
            a+=letter
    new_data.append(a)

with open("new_word.txt","w") as file:
    for line in new_data:
        file.write(line)