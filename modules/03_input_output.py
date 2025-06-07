# 03_input_output.py

"""
How to take input from the user and handle different data types.
"""

# By default, input() returns a string
num = input("Enter some value: ")
print("You entered:", num)
print("Type:", type(num))

# Convert to integer
num = int(input("Enter an integer value: "))
print("Integer multiplied by 10:", num * 10)

# Convert to float
num = float(input("Enter a float value: "))
print("Float times 2:", num * 2)
