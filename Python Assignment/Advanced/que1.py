with open("doc.txt", "r") as file:
    for line in file.readlines():
        print(line.strip())