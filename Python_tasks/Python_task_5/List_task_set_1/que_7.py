# program 7 : pairwise product of two list


# creating new lsits
l1 = [1, 2, 3, 4, 5]
l2 = [2, 2, 2, 2, 2]

# product_list
product = []

for i in range(len(l1)):
    product.append(l1[i] * l2[i])
    

print(product)