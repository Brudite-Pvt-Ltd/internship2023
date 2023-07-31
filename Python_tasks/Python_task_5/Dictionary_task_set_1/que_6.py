# program 6 : sort with values


# creating a dictionary
dic = {"viper" : 24, "mitsuha": 23, "esdeath": 24, "shin":21, "isagi" : 20} 

dic = sorted(dic.items(), key = lambda x : x[1])

dic = dict(dic)

print(dic)