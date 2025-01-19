import sys


'''
Problem statement:

Part 2:
Write a Python program to find the multiplication and division of two numbers.

Ask the user to input two numbers (num1 and num2). Given those two numbers, 
multiply them together to find the output. Also, divide num1/num2 to find the output.
'''

# python supports 2 numeric types: int, float.
# Specific numeric Data types are not mentioned in the problem statement.
# Here, I'll provide code for both data types.
# To run with float data type, please uncomment the 2 lines of code for 'float' inside 'try' block.
#
# Assumption:
# Python's integer type (int) has arbitrary precision, so detecting overflow in numeric 
# operation, normally not needed. If you think, I should provide the logic for overflow 
# condition, then please let me know, I'll provide that logic.

redoInput = True # We'll let user try again if incorrect input provided

while redoInput:        
    try:
        # Read user inputs and validate
        num1 = int(input('Enter your first number:\n'))     # for 'int' data types
        num2 = int(input('Enter your second number:\n'))    # for 'int' data types
        #num1 = float(input('Enter your first number:\n'))  # for 'float' data types
        #num2 = float(input('Enter your second number:\n')) # for 'float' data types
        redoInput = False
    except ValueError:
        print('Please try again with numeric inputs.')
        redoInput = True

# multiplication of the two numbers
print('The Multiplication: firstInput * secondInput: ', num1, ' * ', num2, ' = ', num1 * num2)

# division of the two numbers
if num2 == 0:
    print('Division by 0 is not allowed.')
    print('For Division, please rerun the program with input2 as a non-zero numeric input.')
else:
    print('The Division: firstInput / secondInput: ', num1, ' / ', num2, ' = ', num1 / num2)
