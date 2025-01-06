
from array import *
arr=[1,2,3,4,5,6,7]
target=4
for i in range(0,len(arr)):
    if arr[i]==target:
        print(i)
        break
else:
    print("Target not found") 