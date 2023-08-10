# 9. wap to ask user to define even numbers from a list 
num=[1,2,3,4,5,6,7,8,9]
try:
    a=int(input("enter number"))
    if a%2==0:
         print("yes")
    else:
        print("no")
   
except Exception as exception:
    print(exception)
        
finally:
    print("plz choose values from list=[1,2,3,4,5,6,7,8,9]")
        

