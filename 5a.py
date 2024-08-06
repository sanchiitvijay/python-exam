my_tuple = (1, 2, 3, 4, 5)

new_tuple = my_tuple + (6,)
print("Tuple after adding an item:", new_tuple)

print("Length of the tuple:", len(new_tuple))

item = 3
if item in new_tuple:
    print(f"{item} is present in the tuple.")
else:
    print(f"{item} is not present in the tuple.")

index = 2
if 0 <= index < len(new_tuple):
    print(f"Item at index {index}: {new_tuple[index]}")
else:
    print(f"Index {index} is out of range for the tuple.")
