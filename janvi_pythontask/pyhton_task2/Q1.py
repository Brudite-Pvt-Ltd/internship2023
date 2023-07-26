#1. Create an array of the first 10 even numbers (starting from 2).
'''for i in range (2,11):
    if i % 2 ==0:
     print(i,end=" ")'''

even_no=[2*i for i in range(1,11)]
print(even_no)