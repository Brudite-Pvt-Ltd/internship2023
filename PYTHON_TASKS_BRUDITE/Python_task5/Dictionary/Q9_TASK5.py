# Create a function that takes as tring as input and returns the most common
# character and its frequency using a dictionary

def freq(string):
    freq_dict = {}
    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    freq_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    return freq_dict[0]