# Creation of List

List = []
print("Blank List: ")
print(List)

List = [190, 230, 124,560,192]
print("\nList of numbers: ")
print(List)

List = ["Siya", "rama", "neha"]
print("\nList Items: ")
print(List[0])
print(List[1])

# use of append in python 
my_list = ['play', 'sing', 'dance']

another_list = ['cook', 'code', 'drive']
                
my_list.append(another_list)

print(my_list)


# use of extend 
my_list = ['happy', 'sad']

my_set = {'emotions'}
my_list.extend(my_set)

print(my_list)

# use of index in list
list = ['flag ', 'resister', 'ips', 'pin', 'lines']

print(list.index('ips'))


# use of .clear()
lis = [1, 2, 3]
lis.clear()
print(lis)
