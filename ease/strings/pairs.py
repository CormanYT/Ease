class pair_data:
    def __init__(self, string, start, end):
        self.string = string
        self._span = (start, end)
    def __str__(self):
        return self.string
    def __len__(self):
        return len(self.string)
    def getSpan(self):
        return self._span
def pairs(original=None, one=None, two=None):
    if original == None:
        raise ValueError("You cannot get a pair of nothing!")
    if one == None:
        raise ValueError("You cannot get a pair from nothing!")
    if two == None:
        two = one
    count = 0
    start = 0
    end = 0
    index = 0
    ins = False
    results = []
    if one == two:
        for char in list(original):
            if char == one:
                count += 1
                if count == 1:
                    start = index
                elif count == 2:
                    end = index
                    count = 0
                    charlist = list(original)
                    newly = charlist[start + 1:end]
                    results.append(pair_data("".join(newly), start + 1, end))
            index += 1
    else:
        for char in list(original):
            if char == one:
                count += 1
                if count == 1:
                    start = index
            if char == two:
                count -= 1
                if count == 0:
                    start += 1
                    end = index
                    charlist = list(original)
                    newly = charlist[start:end]
                    results.append(pair_data("".join(newly), start, end))
            index += 1
    return results
