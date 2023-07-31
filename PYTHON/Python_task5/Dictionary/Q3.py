# Extract unique values in a given Dictionary
# D1 = {'list1' : [4,7,10,20] ,'list2' : [7,16,9,10] ,'list3' : [13,10,4,8] ,'list4' : [7,20,6,11]}

def unique_val(dict):
    val = set()
    for name, value in dict.items():
        for i in value:
            if i not in val:
                val.add(i)
    return list(val)

D1 = {'list1' : [4,7,10,20] ,'list2' : [7,16,9,10] ,'list3' : [13,10,4,8] ,'list4' : [7,20,6,11]}
print(unique_val(D1))