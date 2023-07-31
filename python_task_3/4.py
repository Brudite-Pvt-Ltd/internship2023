# Search  the elements from a list of list
list=[[2,3,4],[3,5,6],[4,5,7],[4,6,8],[5,8,9],[2,4,5]]
t=9 
count=0
for x in list:
    for i in x:
        if i==t:
            count += 1
            print(count)    
