"""#10.Given a list of strings, write a function to find the two strings with the highest similarity score. The similarity score 
is defined as the number of common characters between two strings. """
from collections import Counter

def similarity_checker(s1,s2):
    common_character =0
    for key,value in s1.items():
        if key in s2:
            common_character += min(s1[key],s2[key])
    return common_character
#similarity_checker(dict(Counter('vipvuavl')),dict(Counter('dt')))

def string_with_highest_similarity(l):
    hi_smlrty = 0
    best_string =list()
    for i in range(len(l)):
       for j in range(i + 1, len(l)):
            score = similarity_checker(dict(Counter(l[i])),dict(Counter(l[j])))
            if score > hi_smlrty:
                hi_smlrty = score
                best_string.clear()
                best_string.append((l[i],l[j]))
            elif score == hi_smlrty:
                best_string.append((l[i],l[j]))
    return [best_string,hi_smlrty]       

l = ["vipul","vaibhav","vishal","tanmayj ","Yuvraj shamra"]
print(string_with_highest_similarity(l))