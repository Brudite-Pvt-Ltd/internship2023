sentence=str(input("Enter your sentence:  "))
a = sentence.split(" ")
a=a[::-1]
reverse_sentence=""
for words in a:
    reverse_sentence += words + " "
print(reverse_sentence)
