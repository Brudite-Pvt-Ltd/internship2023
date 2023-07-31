# program 10 :
    

# creating a list of string with lower case latters
l1 = ["abccde", "ab", "aabbcc", "abcdd", "abcce"]


# using a lookup to store the count of each character for every string
lookUp = [ [0 for _ in range(26)]  for _ in range(len(l1))]


# setting the lookup.
for i in range(len(l1)):
    for ch in l1[i]:
        lookUp[i][ord(ch) - 97] += 1


# fuction to find the similarity_score between two strings
def get_score(a, b, i, j, lookUp):
    
    score = 0 
    
    # iterating in lookUp table to find the occurance of a character
    for x in range(0, 26):
        score += min(lookUp[i][x], lookUp[j][x])
        
    return score;


# creating ans_strings and similarity_score variables to store the answers
ans_str1 = ""
ans_str2 = ""
s_score = 0 

for i in range(len(l1)):
    for j in range(i+1, len(l1)):
       
        # score between two strings 
        s = get_score(l1[i], l1[j], i, j, lookUp)
        
        # storing the answer if it's score is more then our stored answer
        if( s > s_score ):
            s_score = s 
            ans_str1 = l1[i]
            ans_str2 = l1[j]        
    
print("Strings are : ", ans_str1, ans_str2)
print("With score : ", s_score)

