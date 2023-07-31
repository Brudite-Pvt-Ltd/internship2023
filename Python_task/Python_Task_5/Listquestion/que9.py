#9.Find the maximum difference between any two elements in a list

l = [4,7,3,90,37,12,11]

#method1 
print(max(l)-min(l))

#method2
l.sort()
print(l[len(l)-1]-l[0])

#method 3
maximum = -100
minimum = 1000

for x in l:
    if x > maximum:
        maximum = x
for x in l:
    if x < minimum:
        minimum = x
        
print(maximum-minimum)
        