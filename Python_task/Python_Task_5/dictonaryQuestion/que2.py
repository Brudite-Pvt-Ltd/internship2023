#2.Write a Python program that takes a sentence as input and counts the frequency of each word using a dictionary.

sentence = input("enter a sentence:-")
dict1 = {}
for x in sentence:
    if x in dict1:
        dict1[x] += 1
    else:
        dict1[x] =1
print(dict1)

dict2={}
dict2 =sentence.fromkeys()
print(dict2)