#Calculate the pairwise product of two lists'
l1 = [1,2,3,4]
l2 = [4,3,2,1]
products = []
for i in range(len(l1)) :
    for j in range(len(l2)) :
        products.append(l1[i] * l2[j])
print(products)