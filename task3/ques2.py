# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 17:48:58 2023

@author: visha
"""


def sort(list):
    i=0
    j=0
    for i in range(0,len(list)):      
        for j in range(len(list)):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
             
    return list       
            
l1=[[2,4],[7,8],[9,10]]
l2=[[4,2],[8,9],[9,10]]
nl1=[]
nl2=[]
uncommon_list=[]
for i in l1:
    nl1.append(sort(i))
for i in l2:
    nl2.append(sort(i))


for x in nl1:
    flag = 0
    for y in nl2:
        if x==y:
            flag = 1
        
    if flag == 0:     
        uncommon_list.append(x)
for y in nl2:
    flag = 0
    for x in nl1:
        if y==x:
            flag = 1
      
    if flag == 0 :    
        uncommon_list.append(y)
            
print(uncommon_list)




# def sort(list):
#     i=0
#     j=0
#     for i in range(0,len(list)):      
#         for j in range(len(list)):
#             if list[i]>list[j]:
#                 list[i],list[j]=list[j],list[i]
             
#     return list       
            
# l1=[[2,4],[7,8],[9,10]]
# l2=[[4,2],[8,9],[9,10]]
# nl1=[]
# nl2=[]
# uncommon_list=[]
# for i in l1:
#     nl1.append(sort(i))
# for i in l2:
#     nl2.append(sort(i))


# for x in nl1:
#     for y in nl2:
#         if x!=y:
#             uncommon_list.append(x)
# for y in nl2:
#     for x in nl1:
#         if y!=x:
#             uncommon_list.append(y)
            
# uc=[]            
# for i in uncommon_list:
             
#     uc.append(tuple(i))         
       
        
# from collections import Counter
 
# counter = Counter(uc)


# ans = []
# for (key, val) in counter.items():
#     if(val == 3):
#         ans.append(list(key))
# print(ans)                   



  

  