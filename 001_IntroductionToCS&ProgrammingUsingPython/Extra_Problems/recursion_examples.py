"""
@author: Anirudh Sharma
"""


# Example #1 - Multiplying iteratively and recursively

def multiply_iteratively(a, b):
    '''
    This method just multiplies two numbers using iteration
    '''
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

a, b = int(input("Enter first number: ")), int(input("Enter second number: "))
print("Product of", a, "and", b, "is:",multiply_iteratively(a, b))


def multiply_recursively(a, b):
    '''
    This method multiplies two numbers recursively
    '''
    if(b == 1):
        return a
    else:
        return a + multiply_recursively(a, b - 1)
    
c, d = int(input("Enter first number: ")), int(input("Enter second number: "))
print("Product of", c, "and", d, "is:", multiply_recursively(c, d))
