def merge_sort(arr):
    if len(arr) <= 1:  # Base case: A single element is already sorted
        return arr

    # Step 1: Divide the array
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])   # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half

    # Step 2: Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Compare elements and merge in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Add remaining elements from both halves
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array

# Example usage
arr = [8, 4, 6, 2, 9, 5]
print("Original array:", arr)

sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
