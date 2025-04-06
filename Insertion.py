def insertion_sort(arr):
    for i in range(1, len(arr)):  # Start from the second element
        key = arr[i]  # Element to be inserted
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # Insert key at the correct position

# Example usage:
arr = [8, 4, 6, 2, 9]
print("Original array:", arr)

insertion_sort(arr)
print("Sorted array:", arr)
