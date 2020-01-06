"""
@author: Anirudh Sharma
"""

def bisection_cuberoot_approx(n, epsilon):
    low = 0.0
    high = n
    guess = (low + high) / 2.0
    
    while abs(guess**3 - n) >= epsilon:
        if guess**3 < n:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
    
    return guess

# Loop for various numbers to find their cuberoot
x = 1
while x <= 10000:
    approx = bisection_cuberoot_approx(x, 0.01)
    print(approx, "is close to cube root of", x)
    x *= 10