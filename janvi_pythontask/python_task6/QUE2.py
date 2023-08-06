def create_unique_list(list):
    unique_list=[]
    unique_list = set(list)
    return unique_list


list = [1,2,2,3,4,4,5,5]
new_list = create_unique_list(list)
print("New list with unique elements:", new_list)