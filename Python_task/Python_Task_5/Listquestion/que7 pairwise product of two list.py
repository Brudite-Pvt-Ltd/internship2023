#7. calculate the pairwise product of two list

l1 =[1,3,5,6,33,4,9]
l2 =[9,4,2,6,7,5,2]

#method 1
l3 = [ l1[i]*l2[i] for i in range(len(l1))]
print(l3)

#method 2
l4 = list(map(lambda x,y:x*y,l1,l2))
print(l4)


