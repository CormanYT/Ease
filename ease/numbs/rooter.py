from fractions import fr, toFr
def _np(a, b):
    c = [1]
    while True:
        if (c[-1] ** b) > a:
            return (c[-1], c[-2])
        c.append(c[-1] + 1)
def root(a, b):
    numbs = _np(a, b)
    def rootTry(c, d):
        first = fr(c, d)
        d = toFr(d).simplify()
        this = d + first
        return this / 2
    newroot = rootTry(a, numbs[1])
    for x in range(100):
        newroot = rootTry(a, newroot)
    return newroot

t = root(10, 2)
