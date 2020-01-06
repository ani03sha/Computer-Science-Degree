"""
@author: Anirudh Sharma
"""

# Reading a number from the user
n = float(input("Enter a number for which we want to find cube root: "))

# Low index for bisection search
low = 0
# High index for bisection search
high = 1 if n < 1 else n
print(high)
# Value of epsilon
epsilon = 0.00000001
# Number of guesses
number_of_guesses = 0

# Guess values
guess = (low + high) / 2.0

# Loop until we do not lie under the accepted epsilon value
while abs(guess**3 - n) >= epsilon:
    if guess**3 < n:
        # look only in upper half search space
        low = guess
    else:
        # look only in lower half search space
        high = guess
    # next guess is halfway in search space
    guess = (low + high) / 2.0
    number_of_guesses += 1

print('Number of guesses =', number_of_guesses)
print(guess, 'is close to the cube root of', n)


