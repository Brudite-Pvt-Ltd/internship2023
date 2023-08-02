#4.Write a function that takes a dictionary and returns a list of keys whose values are greater than a given number.
def key_greater_than_values(student,value):
    key_greater=dict()
    for x,y in student.items():
        if y>value:
            key_greater=x
            return key_greater

student={'ank': 80,'nav': 78,'janvi':82,'harshii':89}
value=int(input("enter the value"))
above_value=key_greater_than_values(student,value)
print("list of keys whoes values are greater than the given value :-",above_value)