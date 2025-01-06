#Linear search (1)
from array import *
arr=[1,2,3,4,5,6,7]
target=4
for i in range(0,len(arr)):
    if arr[i]==target:
        print("Target is 4 and its index is:",i)
        break
else:
    print("Target not found") 

#Linear search 2
array=[1,2,3,4,5]
x=2
for i in array:
    if i==x:
        print("yes",i)
else:
    print ("No")

#Binary search using function
def binary_search(arr, target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return -1
array=[5,10,15,20,25,30,45,60,75]
target=60
result=binary_search(array, target)
if result!=-1:
    print(f"the target found at {result}")
else:
    print("Target not found")

#Binary search using recursion function
def binary_search_recursive(arr, target, low, high): 
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

def binary_search(arr, target):
    return binary_search_recursive(arr, target, 0, len(arr) - 1)

# Example Usage
array = [12, 13, 14, 15, 16, 17, 18]
target = 12
result = binary_search(array, target)
if result != -1:
    print(f"The target found at index {result}")
else:
    print("The target not found")
