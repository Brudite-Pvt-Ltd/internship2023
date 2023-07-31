# program 4 : updating the key


# creating a dictionary
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

i = input('Enter the old key : ')
j = input('Enter the new key : ')

dic[j] = dic.pop(i)

print(dic)
