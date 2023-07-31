kuchbhi = set (["3","5","7"])
print(kuchbhi) #prints the set items

kuchbhi.add("11")  #adds the item to the set
print(kuchbhi)  

kuchbhi2=kuchbhi.copy()  #copy the set items
print(kuchbhi2)

kuchbhi2.discard("3")  #discards the specified item
print(kuchbhi2)

kuchbhidiff = kuchbhi.difference(kuchbhi2)  #returns set containing difference between two
print(kuchbhidiff)

kuchbhi.clear()  #clear the set
print(kuchbhi)