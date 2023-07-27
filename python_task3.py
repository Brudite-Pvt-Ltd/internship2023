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



#Question 2--------------------------------------------
def find_uncommon_pairs(list1, list2):
    uncommon_pairs = [pair for pair in list1 if pair not in list2] + [pair for pair in list2 if pair not in list1]
    return uncommon_pairs


list1 = [[2, 4], [7, 8], [9, 10]]
list2 = [[4, 2], [8, 9], [9, 10]]

uncommon_pairs = find_uncommon_pairs(list1, list2)
print("Uncommon pairs:")
for pair in uncommon_pairs:
    print(pair)


#QUestion 3 ---------------------------------------------

list1=[[6,1,4],[9,8,14],[8,9,7]]
list2=[]
for x in list1:
    n=len(x)
    for i in range(n):
        for j in range(n):
            if(x[i] >x[j]):
                (x[i], x[j]) = (x[j], x[i])

    list2.append(x)

print("new reverse list :-", list2)

#Question 4 ---------------------------------------------

list1= [[6,1,4,9],[9,8,14,1],[8,2,9,7]]
count = 0
val=input("enter the number that ypu want to search ")
for i in list1:
    for j in i:
        if val==j:
            count+=1
      


if(count>0):
    print(val , "is present")
    print("count :-", count)

else:
    print(val ,"not present")


#Question 5 ----------------------------------------------
def find_sorted_list(mat):
    transposed_matrix=list(zip(*mat))

    sorted_col=[sorted(col) for col in transposed_matrix]
    sorted_matrix = list(zip(*sorted_col))   

    return sorted_matrix




matrix=[[6,15,10],[14,9,12],[2,4,6]]
 

sorted_mat=find_sorted_list(matrix)
for row in sorted_mat:
    print(row)

#Question ------------------------------------------------

'''list=[(1,2),(2,4),(4,5),(4,2),(1,2)]
set=set()
for x in list:
    if x is not set:
       set.add(x)

print(set)'''


