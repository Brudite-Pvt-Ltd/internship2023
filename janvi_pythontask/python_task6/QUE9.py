def perform_operation_on_list(input_list, index, operation):
    try:
        result = operation(input_list[index])
        return result
    except IndexError:
        print("Index is out of range!")

# Test the function
my_list = [10, 20, 30, 40, 50]

index_to_access = int(input("Enter an index: "))
operation_to_perform = lambda x: x * 2  # Example operation, you can replace with any operation you want

result = perform_operation_on_list(my_list, index_to_access, operation_to_perform)
print(f"Result: {result}")