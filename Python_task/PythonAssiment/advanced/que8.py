"""
que8
You need to write a function that accepts an encoded string as a parameter. This string will contain 
a first name, last name, and an id.Values in the string can be separated by any number of zeros.
The id is a numeric value but will contain no zeros. The function should parse the string and return
a Python dictionary that contains the first name, last name, and id values.
An example input would be “Robert000Smith000123”. The function should return the following using that input:
{ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }

"""
def encodectodict(s):
    l = [x for x in s.split('0') if x != '']
    dict1 = {}
    dict1["first_name"] = l[0]
    dict1["last_name"] = l[1]
    dict1["id"] = l[2]
    return dict1
    # d['first_name']

print(encodectodict('Robert000Smith000123'))