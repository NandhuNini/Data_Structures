import random
def Quicksort(arr):
  if len(arr)<=1:
    return arr  
  pivot=random.choice(arr)
  left=[i for i in arr if i<pivot]
  right=[i for i in arr if i>pivot]
  middle=[i for i in arr if i == pivot]
  return Quicksort(left)+middle+Quicksort(right)
arr=[5,3,2,8,1,6,4,7]
print("Before sort:",(arr))
print("after sorting:",Quicksort(arr))