city_set = {"haridwar", "mathura", "kaashi", "ayodhya"}
vowels = {'a', 'e', 'i', 'o', 'u'}
common= set.intersection(*(set(filter(lambda x: x in vowels,i)) for i in city_set))
print(common)




