#6.Create a set of cities and find the common vowels present in their names
'''city = {'jaipur','jodhpur', 'bikaner'}

vowels= {'a','e','i','o','u'}
for vowels in set:
  set_of_vowels.appendm (set.intersection, vowels)
  print (set_of_vowels)
common_vowels= [set(city.lower()).intersection(vowels)]
common_cities= city.intersection(common_vowels)
print(common_cities)'''

def find_common_vowels(cities):
    vowels = set('aeiou')
    common_vowels = set()
    for city in cities:
        common_vowels.update(filter(lambda x: x in vowels, city.lower()))
    return common_vowels

#  set of cities
cities = {'Jaipur', 'Bikaner', 'Jodhpur',  'Udaipur'}

# Finding the common vowels in the city names
common_vowels = find_common_vowels(cities)

print("Common vowels in the city names:", common_vowels)