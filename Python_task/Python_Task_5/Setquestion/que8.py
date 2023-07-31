#8.create a set of word from a text file and count the occurence of each word in the set.

from collections import Counter
with open('text.txt',"r") as file:
    content = file.read()

word_set =content.split()
print(dict(Counter(set(word_set))))