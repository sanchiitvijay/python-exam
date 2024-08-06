strings = ["apple", "banana", "cherry", "grape"]

# convert list to tuple
tuple_list = [(string, len(string)) for string in strings]

# sort tuple by length of strings
sorted_tuple_list = sorted(tuple_list, key=lambda x: x[1])

print("List of tuples sorted by length of strings:")
print(sorted_tuple_list)
