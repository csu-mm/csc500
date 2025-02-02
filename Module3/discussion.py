#import numpy as np

# to use pip/import: first run the following 2 commands at the terminal prompt
# 1. python -m venv env
# 2. .\env\Scripts\activate



# Python does not have built-in support for arrays like some other programming languages.
# We can use lists to achieve similar functionality.
# Otherwise, we can use the array module or libraries like NumPy.

# use of array module
import array

# use of array from numpy
import numpy as np


my_int_array1 = array.array('i', [1,2,3,4,5])
print(my_int_array1)
my_int_array1[2] = -10
my_int_array1[-1] = -100
print(my_int_array1)

# array module in Python doesn't directly support arrays of strings
my_daysofweek_array = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
print(my_daysofweek_array)
#print or do any operation with array elements in loop
for item in my_daysofweek_array:
    print(item)

numpy_2darray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(numpy_2darray)
print('row 1, col 2: element', numpy_2darray[1][2])
print(numpy_2darray[1][2])

# find max element in 2d array with numeric elements
# find average value of elements in 2d array with numeric elements
max_element = numpy_2darray[0][0]
elementCount = 0
element_sum = 0
for r in numpy_2darray:
    for element in r:
        elementCount += 1
        element_sum += element
        if max_element < element:
            max_element = element

print('Biggest element in numpy_2darray is: ', max_element)
print('Average element value in numpy_2darray is: ', element_sum/elementCount)
