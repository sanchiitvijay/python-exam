import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Original 2D Array:")
print(arr)

print("\nArray elements in reverse order:")
print(arr[::-1, ::-1])

print("\nPrincipal diagonal elements:")
print(np.diag(arr))

sorted_asc = np.sort(arr, axis=None)
print("\nSorted 2D Array in ascending order:")
print(sorted_asc.reshape(arr.shape))

sorted_desc = np.sort(arr, axis=None)[::-1]
print("\nSorted 2D Array in descending order:")
print(sorted_desc.reshape(arr.shape))
