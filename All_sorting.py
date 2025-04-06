arr=[1,10,11,5,2]
for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1):
        #if arr[j]<arr[j+1]:
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

""" def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Track if any swap happens
        swapped = False
        # Perform comparisons and swaps for the unsorted part
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:  # Change > to < for descending order
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, the list is sorted
        if not swapped:
            break
    return arr

# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted list:", data)
sorted_data = bubble_sort(data)
print("Sorted list:", sorted_data) """

arr=[5,4,3,2,1]
while(True):
    a=True
    for j in range(0, len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
        a=False
    if a==True:
        break
print(arr)