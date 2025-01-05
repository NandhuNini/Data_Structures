"""
from array import *
arr=[1,2,3,4,5,6,7]
target=4
for i in range(0,len(arr)):
    if arr[i]==target:
        print(i)
        break
else:
    print("Target not found") 
    """

def linear_search(arr, target):
    """
    Perform a linear search on the given array.

    Parameters:
        arr (list): The array to search.
        target: The value to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    for index, element in enumerate(arr):
        if element == target:
            return index  # Return the index where the target is found
    return -1  # Return -1 if the target is not found

# Example Usage
arr = [10, 20, 30, 40, 50]
target = 30

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")
