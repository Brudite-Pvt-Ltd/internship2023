def key_greater_than_values(student,value):
    key_greater=dict()
    for x,y in student.items():
        if y>value:
           key_greater[x] = y
    return key_greater

student={'nav': 80,'laksh': 78,'harsh':82,'man':89}
value=int(input("enter the value"))
above_value=key_greater_than_values(student,value)
print("list of keys whoes values are greater than the given value :-",above_value)
