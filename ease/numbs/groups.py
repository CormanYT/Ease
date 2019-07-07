from fractions import *
import mathy

def deepStr(obj):
    try:
        iter(obj)
        a = []
        for x in obj:
            if isinstance(a, list):
                a.append(deepStr(x))
            else:
                a = a + deepStr(x)
        return a
    except:
        return str(obj)

def rGroup(numb, length):
    a = []
    for x in range(length):
        a.append(numb)
    return Group(a)
class Group:
    def __init__(self, *args):
        if isinstance(args[0], tuple):
            self.numbs = args[0]
        elif isinstance(args[0], list):
            self.numbs = args[0]
        else:
            self.numbs = args
        self.index = 0
    def __str__(self):
        return "GROUP OF {}".format(str(self.numbs)[1:len(str(self.numbs)) - 1])
    def __order__(self, group):
        if not len(self.numbs) > (len(group.numbs) - 1):
            raise ValueError("Incorrect length.")
        this = []
        for x in range(len(self.numbs)):
            if not (group.numbs[x]) is None:
                this.append((self.numbs[x], group.numbs[x]))
            else:
                this.append(self.numbs[x])
        return this
    def __add__(self, group):
        compare = self.__order__(group)
        lister = []
        for x, y in compare:
            try:
                lister.append(x + y)
            except:
                lister.append(x)
        return Group(lister)
    def __sub__(self, group):
        compare = self.__order__(group)
        lister = []
        for x, y in compare:
            try:
                lister.append(x - y)
            except:
                lister.append(x)
        return Group(lister)
    def __mul__(self, group):
        compare = self.__order__(group)
        lister = []
        for x, y in compare:
            try:
                lister.append(x * y)
            except:
                lister.append(x)
        return Group(lister)
    def __truediv__(self, group):
        compare = self.__order__(group)
        lister = []
        for x, y in compare:
            try:
                lister.append(x / y)
            except:
                lister.append(x)
        return Group(lister)
    def __pow__(self, group):
        compare = self.__order__(group)
        lister = []
        for x, y in compare:
            try:
                lister.append(x.__pow__(y))
            except:
                lister.append(x)
        return Group(lister)
    def __sum__(self):
        a = 0
        for x in self:
            a += x
        return a
    def __len__(self):
        return len(self.numbs)
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        try:
            return self.numbs[self.index - 1]
        except:
            raise StopIteration
a = fr(1, 2)
b = mathy.fractionRoot(a, 2)
