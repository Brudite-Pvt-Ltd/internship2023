#Question 4 ---------------------------------------------

list1= [[6,1,4,9],[9,8,14,1],[8,2,9,7]]
count = 0
val=input("enter the number that ypu want to search ")
for i in list1:
    for j in i:
        if int(val)==j:
            count=count+1
      


if(count>0):
    print(val , "is present")
    print("count :-", count)

else:
    print(val ,"not present")
