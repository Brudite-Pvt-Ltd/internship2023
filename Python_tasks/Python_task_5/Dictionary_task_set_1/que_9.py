# program 9 :

my_dic = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red', 'grapes': 'purple', 'orange': 'orange'}

dic = sorted(my_dic.items(),  key = lambda x : len(x[1]) )

my_dic = dict(dic) 

print(my_dic)