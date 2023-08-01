wc = {}
uw = set()

with open('V:\sample.txt', 'r') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            uw.add(word)
            wc[word] = wc.get(word, 0) + 1

# Print the unique words and their occurrences
print("Unique Words in file are :", uw)
print("Word Count is :", wc)

