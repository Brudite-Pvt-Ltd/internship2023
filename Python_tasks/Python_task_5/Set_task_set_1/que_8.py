# program 8 : 
    

# creating a set of words from text file 

file =  open("X:/proCPP/temp.txt", "r")

# converting it into list of string
string = file.read()
s = string.split(' ')

# creating a set of words
word_set = set(s)

# creating empty dictionary
dic = {}

# storing there count in dictionary
for x in word_set:
    dic[x] = dic.get(x, 0) + 1


# we stored the word in set so there occurance will be 1 always.
for x,y in dic.items():
    print(x, " : ", y)    