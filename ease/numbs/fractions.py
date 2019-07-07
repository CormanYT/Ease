import numbers
print()
import math
print()
import mathy
print()
import random
print()
import time
print()
import re
print()
import os, sys, inspect
print()
import operations
print()

#Go to parent directory

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

#Import things from parent directory

from sets.shared import shared

#Back to current directory

sys.path.insert(0, currentdir)


class Fraction(numbers.Rational):

    #Initialize
    
    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den

    #Get the numerator or denominator, simplify the fraction or use the basic 4 operations on it.

    def numerator(self):
        return self.numerator
    def denominator(self):
        return self.denominator

    def simplify(self):
        divideBy = operations.gcd(self.numerator, self.denominator)
        return Fraction(round(self.numerator / divideBy), round(self.denominator / divideBy))
    def invert(self):
        return Fraction(self.denominator, self.numerator)
    def compare(self, fraction):
        if isinstance(fraction, Fraction):
            denom = operations.lcm(self.denominator, fraction.denominator)
            one = (denom / self.denominator) * self.numerator
            two = (denom / fraction.denominator) * fraction.numerator
            return [one, two]
        elif isinstance(fraction, numbers.Number):
            return self.compare(toFr(fraction))
    def __str__(self):
        return str(self.numerator) + " / " + str(self.denominator)
    def __add__(self, fraction):
        denom = operations.lcm(self.denominator, fraction.denominator)
        one = (denom / self.denominator) * self.numerator
        two = (denom / fraction.denominator) * fraction.numerator
        return Fraction(one + two, denom)
    def __sub__(self, fraction):
        denom = operations.lcm(self.denominator, fraction.denominator)
        one = (denom / self.denominator) * self.numerator
        two = (denom / fraction.denominator) * fraction.numerator
        return Fraction(one - two, denom)
    def __mul__(self, fraction):
        if isinstance(fraction, Fraction):
            return Fraction(self.numerator * fraction.numerator, self.denominator * fraction.denominator)
        elif isinstance(fraction, int):
            return Fraction(self.numerator * fraction, self.denominator)
    def __truediv__(self, fraction):
        if isinstance(fraction, Fraction):
            return self.__mul__(fraction.invert())
        elif isinstance(fraction, int):
            return self.__mul__(Fraction(1, fraction))
    #Support for reverse operations

    def __radd__(self, fraction):
        return self + fraction
    def __rsub__(self, fraction):
        return fraction - self
    def __rmul__(self, fraction):
        if isinstance(fraction, int):
            return Fraction(self.numerator * fraction, self.denominator)
    def __rtruediv__(self, fraction):
        return fraction / self

    #Convert it to a float, useful.
        
    def __float__(self):
        return self.numerator / self.denominator

    #Extra functions used to allow inheritance of math.Rational
    
    def __trunc__(self):
        return math.trunc(float(self))
    def __floor__(self):
        return math.floor(float(self))
    def __ceil__(self):
        return math.ceil(float(self))
    def __round__(self):
        return round(float(self))
    def __mod__(self, numb):
        return float(self) % float(numb)
    def __rmod__(self, numb):
        return float(numb) % float(self)
    def __lt__(self, numb):
        numbs = self.compare(numb)
        return numbs[0] < numbs[1]
    def __le__(self, numb):
        numbs = self.compare(numb)
        return numbs[0] <= numbs[1]
    def __floordiv__(self, frac):
        return round(self) / round(frac)
    def __rfloordiv__(self, frac):
        return round(frac) / round(self)
    def __abs__(self):
        return toFr(math.abs(float(self)))
    def __eq__(self, numb):
        numbs = self.compare(numb)
        return numbs[0] == numbs[1]
    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)
    def __pos__(self):
        return self
    def __pow__(self, numb):
        return self.pow(numb)
            
    def __rpow__(self, numb):
        return numb.pow(self)
    def pow(self, numb):
        if isinstance(numb, int):
            output = self
            for x in range(numb - 1):
                output = output * self
            return output
        elif isinstance(numb, Fraction):
            first = mathy.decFracRoot(self, numb.denominator)
            one = toFr(first[0])
            two = toFr(first[1])
            output = (one / two).pow(numb.numerator)
            return output
        elif isinstance(numb, float):
            return output.pow(toFr(numb))
        
    
def fr(num, den):
    return Fraction(num, den)
def toFr(num):
    numb = "0" + str(float(num))
    this = numb.split(".")
    denom = "0" * len(this[1])
    denom = "1" + denom
    numbOne = int(this[1])
    numbTwo = int(this[0]) * int(denom)
    return Fraction(numbOne + numbTwo, int(denom))
