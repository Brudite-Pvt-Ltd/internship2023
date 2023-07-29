#Question 1 -------------------------------------------
        #METHOD 1+++++++++++++++
def unique_values(arr):
    uni_val= set(arr)
    return uni_val

list = [2,4,1,5,2,7,8,3,5,2,1,1]
unique_list=unique_values(list)
print("unique values in a list",unique_list)
print("counts :-",len(unique_list))

        # METHOD 2+++++++++++++


list2=[1,3,5,6,1,6]
unique_list = []
unique_items = 0

for item in list2:
     if item not in unique_list:
         unique_list.append(item)
         unique_items += 1

print(unique_items)
print("list of unique item:-", unique_items)

         #METHOD_3+++++++++++++++
dict = {'ramdom' : [9,7,4,8,9,4]}

unq_items = list({ele for val in dict.values() for ele in val})
count = len(unq_items)
print(count)