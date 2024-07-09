def create_tuple_list(strings):
    return [(string, len(string)) for string in strings]

def sort_by_length(tuple_list):
    return sorted(tuple_list, key=lambda x: x[1])

strings = ["apple", "banana", "cherry", "grape"]
tuple_list = create_tuple_list(strings)
sorted_tuple_list = sort_by_length(tuple_list)

print("List of tuples sorted by length of strings:")
print(sorted_tuple_list)
