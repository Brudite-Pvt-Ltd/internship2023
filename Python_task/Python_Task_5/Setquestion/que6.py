#3.Create a set of cities and find the common vowels present in their names

from functools import reduce
s = {'jaipur','ajmeru','Nagpur','udaipur'}
common_characters ={}
vowels =['a','e','i','o','u','A','E','I','O','U']
common_characters=reduce(lambda x,y: set(x).intersection(y),s)
print([x for x in common_characters if x in vowels])