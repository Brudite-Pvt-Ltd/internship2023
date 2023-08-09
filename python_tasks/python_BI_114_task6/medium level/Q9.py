#wap to ask user to add any two numbers from a list 
num=[1,2,3,4,5,6,7,8,9]
try:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    if a in num and b in num:
        sum=a+b
        print(sum)
   
except Exception as exception:
    print(exception)
        
finally:
    print("plz choose values from list=[1,2,3,4,5,6,7,8,9]")
        

