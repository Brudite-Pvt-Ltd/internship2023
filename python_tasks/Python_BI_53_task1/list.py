#  remove method 1
my_list= [1,'nav',2,'man',3,'love',4,'harsh',5,'laksh']
print(my_list)
#now remove operation on list to remove the item
my_list.remove('man')
print("print the modified list")
print(my_list)

# index method 2

index=my_list.index('harsh')
print("print the index of  given input :-",index)

#copy method 3

copy_list=my_list.copy()
print("print the copied list :-", copy_list)

# length method 4

length = len(my_list)
print("print the length of the list",length)

#reverse method 5

my_list2 = [1, 2, 3,4,5]
my_list2.reverse()
print(my_list2)