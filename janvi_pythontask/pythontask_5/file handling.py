'''f =open('sample.txt','r')


print(f)
f.close()'''
 
with open('sample.txt','a') as file:
    text =(file.write('hii'))
    print(text)