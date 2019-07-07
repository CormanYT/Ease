def root(x, y):
    a = 1. / float(y)
    return x ** a

def frRoot(x, y):
    return [x, (1., float(y))]
def fracRoot(x, y):
    return [frRoot(x.numerator, y), frRoot(x.denominator, y)]
def decFracRoot(x, y):
    return [root(x.numerator, y), root(x.denominator, y)]
def fractionRoot(x, y):
    fr = type(x)
    a = fr(1, y)
    return x ** a

#print(root(5, 2))
#print(frRoot(5, 2))
