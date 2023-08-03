def get_char_count(string):
    char_count = {}
    for char in string:
        if char.isalpha() or char.isdigit():  # Include alphabetic and numeric characters
            char = char.lower()  #lowercase
            char_count[char] = char_count.get(char, 0) + 1

    result = {}
    for key, value in char_count.items():
        if value in result:
            result[value].append(key)
        else:
            result[value] = [key]

    sorted_result = dict(sorted(result.items(), key=lambda x: x[0], reverse=True))
    for key in sorted_result:
        sorted_result[key].sort()
    return sorted_result

str_test = "Hello. Hello? HELLO!"
print(get_char_count(str_test))
