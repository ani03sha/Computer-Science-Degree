"""
@author: Anirudh Sharma
"""


class Fraction(object):
    
    def __init__(self, numerator, denominator):
        assert type(numerator) == int and type(denominator) == int
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    
    def __add__(self, other):
        n = self.numerator * other.denominator + other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d)
    
    def __sub__(self, other):
        n = self.numerator * other.denominator - other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d)
    
    def __float__(self):
        return self.numerator / self.denominator
    
    def inverse(self):
        return Fraction(self.denominator, self.numerator)
    
    
a = Fraction(1, 2)
b = Fraction(2, 3)

plus = a + b
print(plus)

minus = a - b
print(minus)

f = float(a)
print(f)

r = Fraction.inverse(b)
print(r)