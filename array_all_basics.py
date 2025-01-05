#creating array
from array import array

# Create an array of integers
arr = array('i', [1, 2, 3, 4, 5])
print("Array:", arr)
# create array of character /string
arra = array('u',['q','a'])
print("Array of character:",arra)

# Typecodes In array
#1: b(signed char 1 byte) -128 to 127
from array import array

arr = array('b', [-128, 0, 127])
print(arr)
#2: B(unsigned char 1 byte) 0 to 255
arr = array('B', [0, 100, 255])
print(arr)

#3: h(signed short 2 bytes) -32768 to 32767
arr = array('h', [-32768, 0, 32767])
print(arr)

#4: H(unsigned  short 2 bytes) 0 tp 65535
arr = array('H', [0, 100, 65535])
print(arr)

#Memory view
arr = array('i', [1, 2, 3])
mv = memoryview(arr)
print(mv.format)  # 'i', the typecode of the array




# >>>>>..........Array Operations.............<<<<<
# Accessing array
arr1=array('b',[1,2,3,4,5])
print("Array:",arr1)
print("First element:",arr1[1])

# Modifying array
arr1[1]=20
print(arr1)

# Append array
arr1.append(6)
print("appended array:",arr1)

# Extend array
arr1.extend([7,8,9])
print("Extended array:", arr1)

# Remove elements
arr1.remove(20)
print("removed array:",arr1)

# Insertion of array
arr1.insert(5,11)
print("After insertion array:",arr1)

# loop for finding element
#arr1.extend([5,5,5])
print(arr1)
a=5
for i in range(0, len(arr1)):
    if arr1[i]==a:
        print(i)
        break


    # <<<<<<<<<<<<<<<<<<OUTPUT>>>>>>>>>>>>>>>
  # PS D:\DSA\Data_Structures> python -u "d:\DSA\Data_Structures\array_all_basics.py"
#Array: array('i', [1, 2, 3, 4, 5])
#Array of character: array('u', 'qa')
#array('b', [-128, 0, 127])
#array('B', [0, 100, 255])
#array('h', [-32768, 0, 32767])
#array('H', [0, 100, 65535])
#i
#Array: array('b', [1, 2, 3, 4, 5])
#First element: 2
#array('b', [1, 20, 3, 4, 5])
#appended array: array('b', [1, 20, 3, 4, 5, 6])
#Extended array: array('b', [1, 20, 3, 4, 5, 6, 7, 8, 9])
#removed array: array('b', [1, 3, 4, 5, 6, 7, 8, 9])
#After insertion array: array('b', [1, 3, 4, 5, 6, 11, 7, 8, 9])
#array('b', [1, 3, 4, 5, 6, 11, 7, 8, 9])
#3!