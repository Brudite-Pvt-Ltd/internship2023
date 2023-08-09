def median(list):
    sort_list=(sorted(list))
    print(sort_list)
    n=len(sort_list)
    if n%2==0:
        med=(sort_list[n//2-1]+sort_list[n//2])/2
    return med
    
number_list = [7, 2, 5, 1, 9, 3]
print(median(number_list))
