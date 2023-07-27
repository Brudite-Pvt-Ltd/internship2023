
#reverse sorting

list1 = [[2,1,4],[8,9,7],[2,4,1]]
'''sortedlist = [sorted(innerlist,reversed=True)] 
for innerlist in list1:
    print(sortedlist)'''
'''sortedlist= [sorted( sublist ,reverse=True)] 
for sublist in list1 :
    print(sortedlist)'''
for sublist in list1:
    sublist.sort(reverse=True)
    print(list1)#reverse sorting

list1 = [[6,1,4],[9,8,14],[8,9,7]]
'''sortedlist = [sorted(innerlist,reversed=True)] 
for innerlist in list1:
    print(sortedlist)'''
'''sortedlist= [sorted( sublist ,reverse=True)] 
for sublist in list1 :
    print(sortedlist)'''
for sublist in list1:
    sublist.sort(reverse=True)
    print(list1)