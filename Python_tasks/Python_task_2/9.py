# program 9

array = [1, 2, 3, 4, 5, 6]
pos = int(input())

new_arr = [];

for i in range (pos, len(array)):
    new_arr.append(array[i])
    array[i] = array[i-pos]
    
for i in range(0, len(new_arr)):
    array[i] = new_arr[i];
    

print(array)

