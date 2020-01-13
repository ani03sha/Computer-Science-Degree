"""
@author: Anirudh Sharma
"""

# Example #1

def quotient_and_remainder(a, b):
    q = a // b
    r = a % b
    return (q, r)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Quotient and Remainder of", a, "and", b, "are", 
      quotient_and_remainder(a, b), "respectively")


# Example #2

def get_data(aTuple):
    """
    aTuple, tuple of tuples (int, string)
    Extracts all integers from aTuple and sets 
    them as elements in a new tuple. 
    Extracts all unique strings from from aTuple 
    and sets them as elements in a new tuple.
    Returns a tuple of the minimum integer, the
    maximum integer, and the number of unique strings
    """
    numbers = ()
    words = ()
    for t in aTuple:
         # Concatenating with a singleton tuple
        numbers = numbers + (t[0],)
        # Only add words haven't added before
        if t[1] not in words:
            words = words + (t[1],)
    
    minimumNumber = min(numbers)
    maximumNumber = max(numbers)
    uniqueWords = len(words)
    
    return (minimumNumber, maximumNumber, uniqueWords)

# apply to any data you want!
tswift = ((2014,"Katy"),
          (2014, "Harry"),
          (2012,"Jake"), 
          (2010,"Taylor"), 
          (2008,"Joe"))    
(min_year, max_year, num_people) = get_data(tswift)
print("From", min_year, "to", max_year, \
        "Taylor Swift wrote songs about", num_people, "people!")
