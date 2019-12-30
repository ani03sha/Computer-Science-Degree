"""
@author: Anirudh Sharma
"""

"""
Write a program that does the following in order:
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”.
"""
import math

# Read x from the user
x = float(input("Enter x"))
# Read y from the user
y = float(input("Enter y"))
# x raised to the power y
print(x**y)
# Find log2(x)
print(math.log(x, 2))