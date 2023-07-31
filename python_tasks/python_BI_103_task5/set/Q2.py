print("enter the elements to add until reaches size 10")
set=set()

for i in range(20):
    if len(set)<10:
        ele=input()
        set.add(ele)
    else:
        break
print("new set:-",set)
