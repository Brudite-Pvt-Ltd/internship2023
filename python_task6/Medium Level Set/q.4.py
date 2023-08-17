#The task is to rotate array by D elements towards right
#Sample Input: arr = [1, 2, 3, 4, 5], D = 2
#Sample Output: arr after rotation = [4, 5, 1, 2, 3]
def rotate(R, D, n):
	a = R.index(D)
	list1 = []
	list1 = R[a+1:]+R[0:a+1] 
	return list1


if __name__ == '__main__':
	arr = [1, 2, 3, 4, 5]
	D = 3
	n = len(arr)

	
	arr = rotate(arr, D, n)
	for i in arr:
		print(i, end=" ")
