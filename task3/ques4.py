# def sort(list,n):
    
#     for x in list:
#         for i in x:      
#             if i==n:
#                return True 
#     return False
            
    

# l1=[[1,2,3],[99,399,10,34,45],[69,33,51],[11,90,9]]
# n=int(input("enter the number to be searched"))
# print(sort(l1,n))   


l1=[[1,2,9,3],[9,9,399,10,34,45],[6,9,33,51],[11,90,9]]
n=int(input("enter the number to be searched"))
COUNT=[]
flag = 0
for x in l1:
    for i in x:
        if i == n:
            COUNT.append(i)
            flag = 1
if flag == 0:
    print("NO , entered element is not present in list")
else:
    print("YES , entered element is present in list")  
    print("total number of occurence of entered element is :",len(COUNT))
