# a list with integers, strings, and floats
mixed_data = [1, "esade", 3.14, 92, "Barcelona", 2.718]

# create a new list with only integers from the original list
integers = [item for item in mixed_data if isinstance(item, int)]
print(integers)