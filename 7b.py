import numpy as np

def display_2d_array(arr):
    print("Original 2D Array:")
    print(arr)

def display_reverse_array(arr):
    print("\nArray elements in reverse order:")
    print(arr[::-1, ::-1])

def display_principal_diagonal(arr):
    print("\nPrincipal diagonal elements:")
    print(np.diag(arr))

def sort_array(arr):
    sorted_asc = np.sort(arr, axis=None)
    print("\nSorted 2D Array in ascending order:")
    print(sorted_asc.reshape(arr.shape))

    sorted_desc = np.sort(arr, axis=None)[::-1]
    print("\nSorted 2D Array in descending order:")
    print(sorted_desc.reshape(arr.shape))

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

display_2d_array(arr)
display_reverse_array(arr)
display_principal_diagonal(arr)
sort_array(arr)
