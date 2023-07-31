# program 6 : finding common vowels present in strnings


# creating a set of city names i added 'o' in the end of every city for atleast one common vowel :)

city_set = {"newyorko", "london", "pariso", "tokyo", "sydneyo"}

common_vowels = set()

vowels = { 'a', 'e', 'i', 'o', 'u'}

for x in city_set :
    v = set()
    for y in x :
        if y in vowels:
            v.add(y)
        
    if len(common_vowels) == 0:
        common_vowels = v 
    else :
        common_vowels = common_vowels.intersection(v)
        
print("Common vowels :", common_vowels)