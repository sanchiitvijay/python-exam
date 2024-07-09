def find_max_min(arr):
    max_num = arr[0]
    min_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num

def find_second_largest(arr):
    max_num = arr[0]
    second_max = float('-inf')
    for num in arr[1:]:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    return second_max

arr = [5, 3, 8, 2, 9, 1, 7]

max_num, min_num = find_max_min(arr)
print(f"Maximum number: {max_num}")
print(f"Minimum number: {min_num}")

second_largest = find_second_largest(arr)
print(f"Second largest number: {second_largest}")
