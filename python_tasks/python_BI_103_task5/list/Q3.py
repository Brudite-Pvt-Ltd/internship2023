def freq(list):
    dict1 = {}
    for i in list:
        if i in dict1:
           dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1

list1 = [1,2,23,4,5,6,7,3,4,1,2]
print(freq(list1))