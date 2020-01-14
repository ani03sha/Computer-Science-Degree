"""
@author: Anirudh Sharma
"""


def factorial_iteratively(n):
    result = 1
    for i in range (1, n + 1):
        result *= i
    
    return result

print(factorial_iteratively(6))


def factorial_recursively(n):
    if(n == 1):
        return 1
    return n * factorial_recursively(n - 1)

print(factorial_recursively(9))

