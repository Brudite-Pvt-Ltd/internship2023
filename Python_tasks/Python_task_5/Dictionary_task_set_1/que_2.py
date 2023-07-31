# program 2 : count the freq. of each word using dictionary


# taking input from user

sentence = input('Enter the sentence : ').split()

dic = {}

# inserting the data into dictionary
for x in sentence:
    dic[x] = dic.get(x, 0) + 1


print(dic)