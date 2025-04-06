def heapify(arr, n, i):
    largest = i         # Assume current i is the largest
    left = 2 * i + 1     # Left child index
    right = 2 * i + 2    # Right child index

    # Check if left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Heapify the affected subtree

def heapSort(arr):
    n = len(arr)

    # Step 1: Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

# Example
arr = [5, 4, 3, 6, 8, 9, 1]
print("Before Sorting:", arr)
heapSort(arr)
print("After Heap Sort:", arr)
