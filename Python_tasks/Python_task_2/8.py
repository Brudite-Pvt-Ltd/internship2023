# program 8

# using kadane algo.

array = [1, -3, 5, -2, 3, -1, 9, -8, 6]
max_sum = -1e8
cur_sum = 0 
idx = -1;

for i in range(0, len(array)):    
    cur_sum += array[i]

    if cur_sum > max_sum :
        idx = i 
        max_sum = cur_sum
    
    if cur_sum < 0:
        cur_sum = 0 ;

sub_array = []
new_sum = 0;
for i in range(idx, -1, -1):
    new_sum += array[i]
    sub_array.insert(0, array[i])
    if(new_sum == max_sum):
        break;
        
print(max_sum, sub_array)
    
