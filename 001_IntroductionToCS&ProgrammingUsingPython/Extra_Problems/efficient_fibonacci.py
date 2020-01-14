"""
@author: Anirudh Sharma
"""

def efficient_fibonacci(n, d):
    if n in d:
        return d[n]
    else:
        result = efficient_fibonacci(n - 1, d) + efficient_fibonacci(n - 2, d)
        d[n] = result
        return result
    
d = {1:1, 2:2}
print(efficient_fibonacci(34, d))
    