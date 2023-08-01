from collections import Counter
i=input("enter the sentence")
words = i.split()
frequency=Counter(words)
for x,y in frequency.items():
    print(x,y)