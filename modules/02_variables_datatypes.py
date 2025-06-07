# 02_variables_datatypes.py

"""
This file shows how Python handles variables and datatypes.
"""

# Variables are just references to objects
a = 25
b = 25

print("a =", a)
print("b =", b)
print("id(a):", id(a))
print("id(b):", id(b))  # Same ID → same object in memory

# Checking types
print("Type of a:", type(a))  # <class 'int'>

a = 3.5
print("Now a =", a)
print("Type of a:", type(a))  # <class 'float'>

a = "Hi"
print("Now a =", a)
print("Type of a:", type(a))  # <class 'str'>
