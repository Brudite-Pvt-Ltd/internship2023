

def s_score(s1, s2):
  
    return sum(c1 == c2 for c1, c2 in zip(s1, s2))

def similar(string):
    if len(string) < 2:
        return None, None  
    h_score = -1
    h_pair = None, None

    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            score = s_score(string[i], string[j])
            if score > h_score:
                h_score = score
                h_pair = string[i], string[j]

    return h_pair


l1 = ["vishal", "tarun", "aakash", "sameer", "rahul"]
result = similar(l1)
print("Strings with more common elements:", result)
