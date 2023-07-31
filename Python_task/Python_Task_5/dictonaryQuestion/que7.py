#7.Create a function that takes a list of words and groups them in to a dictionary based on the length of each word

def take_list_of_words(l):
    dict_of_word ={}
    for x in l:
        length_of_word = len(x)
        if length_of_word in dict_of_word:
            dict_of_word[length_of_word].append(x)
        else:
            dict_of_word[length_of_word] = [x]
    return dict_of_word
l = ["vipul", "vishal", "Vaibhav", "Brudite", "Empty", "Null", "Hello-world","Skit"]

print(take_list_of_words(l))