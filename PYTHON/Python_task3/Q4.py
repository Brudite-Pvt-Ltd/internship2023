list=[[6,1,4],[6,8,14],[8,6,7]]

counter = 0
f = int(input('Enter the value to be searched : '))

for i in list:
    for j in i:
        if j == f:
            counter += 1

if counter == 0:
    print('Element not found')

else:
    print(counter)