# Creating a Set
set1 = set("ABCDEFGH")
print("Initial blank Set: ")
print(set1)

# Addition of elements in a Set

set1 = set()
print("Initial blank Set: ")
print(set1)

set1.add(8)
set1.add(9)
set1.add((6, 7))
print("\nSet after Addition of Three elements: ")
print(set1)

for i in range(1, 6):
	set1.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(set1)

# using Update function
set1 = set([4, 5, (6, 7)])
set1.update([10, 11])
print("\nSet after Addition of elements using Update: ")
print(set1)


# Accessing of elements in a set

set1 = set(["access", "elements", "in","set"])
print("\nInitial set")
print(set1)

print("\nElements of set: ")
for i in set1:
	print(i, end=" ")

print("\n")
print("access" in set1)


# Deletion of elements in a Set

set1 = set([1, 2, 3, 4, 5, 6,
			7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)
set1.pop()
print("\nSet after popping an element: ")
print(set1)


