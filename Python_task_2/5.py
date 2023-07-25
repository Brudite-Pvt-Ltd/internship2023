# program 5

array = [1, 2, 3, 4, 5, 8, 7]
flg = 0 
for i in range(1, len(array)):
    if array[i-1] > array[i]:
        flg = 1
        
if(flg):
    print("NOT increasing");
else:
    print("increasing");