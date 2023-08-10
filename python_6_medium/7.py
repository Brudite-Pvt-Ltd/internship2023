# 7.Write a Python function that finds the median of a list of numbers.
# Sample Input: number_list = [7, 2, 5, 1, 9, 3]
# Sample Output: Median: 4.5
def median(list):
    list.sort()
    print(list)
    n=len(list)
    if n%2==0:
        med=(list[n//2-1]+list[n//2])/2
    return med
    
list = [7, 2, 5, 1, 9, 3]
print(median(list))