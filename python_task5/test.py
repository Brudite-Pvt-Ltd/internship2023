'''import math

start = int(input('Enter the start number : '))
end = int(input('Enter the end number : '))

for num in range(start, end+1):
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if(num % i) == 0:
                break;
        else:
            print(num)'''


'''import math

start = int(input("enter the starting value:"))
end = int (input("enter the ending value:"))

for num in range (start,end+1):
    if num >1:
        for i in range (2,int(math.sqrt(num))+1):
            if (num % i) == 0:
                break;
        else:
            print (num)'''



'''list1 =[1,4,7,2,4,8,7,9,10]
list2 = list(set(list1))
list2.sort()
print("Secound largest number of list :",list2[-2])'''


class rectangle():
    def__init__(self):
    self.length = length
    self.breadth = breadth
    
    def area(self):
        return self.length*self.breadth
    a = int(input("Enter the length of rectangle:"))
    b = int(input("enter the breadth of reactangle:"))
    obj = rectangle(a,b);
print("the arae of rectangle is :",obj.area())
        

  



