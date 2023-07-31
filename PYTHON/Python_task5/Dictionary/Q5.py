# Replace Dictionary values from other Dictionary
# Dict1={'a’:1,’b’:2,’c’:3} Dict2={'a’:10,’c’:20,’d’:30

def replace(dict1,dict2):
    for key,value in dict1.items():
        if key in dict2:
            dict1[key]=dict2[key]
        else:
            dict1[key]=value
    return dict1

D1 = {'a':1,'b':2,'c':3}
D2 = {'a':10,'c':20,'d':30}
print(replace(D1,D2))