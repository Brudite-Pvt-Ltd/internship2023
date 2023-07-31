# 5 Create a function that takes two sets and returns their Cartesian product as a set of tuples
setA= (1, 4, 6, 7)
setB = ('a','b')
 
# printing original list and tuple
print("The original setA : " + str(setA))
print("The original setB : " + str(setB))
 
# Construct Cartesian Product
# using list comprehension
result = [(a, b) for a in setA for b in setB]
 
# printing result
print("The Cartesian Product is : " + str(result))