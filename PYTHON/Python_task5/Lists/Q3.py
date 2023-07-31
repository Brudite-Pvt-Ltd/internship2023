# Find the frequency of each element in a list and store it in a dictionary.

def freq(list):
    freq_dict = {}
    for i in list:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    return freq_dict

list = [1, 2, 3, 4, 5, 1, 2, 3]
print(freq(list))