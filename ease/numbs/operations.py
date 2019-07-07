import numbers
from math import sqrt

def difference(one, two):
    this = one - two
    if str(this).startswith("-"):
        that = str(this).lstrip("-")
        return float(that)
    else:
        return this
def closest(one, numbs):
    closest = None
    for item in numbs:
        if closest == None:
            closest = item
        elif difference(one, item) < difference(one, closest):
            closest = item
        elif difference(one, item) == difference(one, closest) and item > closest:
            closest = item
    return closest
def rounding(one, two):
    oner = one / two
    this = round(oner)
    aList = [this]
    if this > oner:
        aList.append(this + 1)
    else:
        aList.append(this - 1)
    return closest(one, aList) * two
def average(numbs):
    return sum(numbs) / len(numbs)
def isNumber(numb):
    return isinstance(numb, numbers.Number)
def multiple(numb, other):
    return (numb % other == 0)
def isPrime(numb):
    for counter, value in enumerate(range(2, round(numb / 2))):
        if multiple(numb, value):
            return False
    return True
def prime(numb):
    for counter, value in enumerate(range(2, round(numb / 2))):
        if multiple(numb, value):
            return value
    return True
def gcd(*args):
    if len(args) == 2:
        a = args[0]
        b = args[1]
        if b == 0:
            return a
        return gcd(b, a%b)
    elif len(args) > 2:
        this = None
        for item in args:
            if newLCM == None:
                newLCM = item
            else:
                newLCM = gcd(newLCM, item)
def lcm(*args):
    if len(args) == 2:
        return args[0] * args[1] / gcd(args[0], args[1])
    else:
        newLCM = None
        for item in args:
            if newLCM == None:
                newLCM = item
            else:
                newLCM = lcm(newLCM, item)
        return newLCM
def factors(numb):
    lower = sqrt(numb)
    factors = []
    final = []
    for x in range(1, int(lower) + 1):
        if multiple(numb, x) == True and x not in factors:
            factors.append(x)
            factors.append(numb // x)
            final.append((x, numb // x))
    return tuple(final)
def full_factors(numb):
    factor = factors(numb)
    them = []
    for x, y in factor:
        them.append(x)
        them.append(y)
    return them
def isPerfect(numb):
    factors = full_factors(numb)
    factors.remove(numb)
    if sum(factors) == numb:
        return True
    return False
def isFactor(one, two):
    return one in full_factors(two)
