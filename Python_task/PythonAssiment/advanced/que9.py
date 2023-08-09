"""
que9
Given an input string, write a function that returns the run length encoded string for the input 
string.
Eg:
Input: wwwwaaadebbbbbw
Output: w4a3d1e1b5w1
"""

def encodedstring(string):
    encoded_string = ''
    cnt = 1
    for i in range(1,len(string)+1):
        if(i==len(string)) or (string[i]!=string[i-1]):
            encoded_string += string[i-1] + str(cnt)
            cnt =1
        else:
            cnt += 1
    return encoded_string
print(encodedstring('wwwwwaaadebbbbw'))
