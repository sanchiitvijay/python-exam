def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    found = False

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            found = True
            break
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    if found:
        print(f"Element {key} found at index {mid}.")
    else:
        print(f"Element {key} not found in the array.")

sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
key = 9

binary_search(sorted_array, key)
