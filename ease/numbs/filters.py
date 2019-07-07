import operations, fractions

class Filter:
    def __init__(self, **kwargs):
        """
        Create a filter with specific qualifications
        """

        
        if "maximum" in kwargs:
            self.max = kwargs["maximum"]
        else:
            self.max = None
        if "minimum" in kwargs:
            self.min = kwargs["minimum"]
        else:
            self.min = None
        if "multiples" in kwargs:
            self.multiples = kwargs["multiples"]
        else:
            self.multiples = None
        if "nonmultiples" in kwargs:
            self.nonmultiples = kwargs["nonmultiples"]
        else:
            self.nonmultiples = None
        if "prime" in kwargs:
            self.prime = kwargs["prime"]
        else:
            self.prime = None
        if "integer" in kwargs:
            self.int = kwargs["integer"]
        else:
            self.int = None
    def check(self, numb):

        "Check if a number meets the qualifications"
        
        if self.max != None:
            if numb > self.max:
                return False
        if self.min != None:
            if numb < self.min:
                return False
        if self.multiples != None:
            for item in self.multiples:
                if operations.multiple(numb, item) == False:
                    return False
        if self.nonmultiples != None:
            for item in self.nonmultiples:
                if operations.multiple(numb, item) == True:
                    return False
        if self.prime == True:
            if operations.isPrime(numb) == False:
                return False
        elif self.prime == False:
            if operations.isPrime(numb) == True:
                return False
        if self.int == True:
            if not isinstance(numb, int):
                return False
        if self.int == False:
            if isinstance(numb, int):
                return False
        return True
    def qualify(self, numbs):

        """numbs is a list of numbers

        This returns a list of the portion of numbs which is qualified

        """
        
        final = []
        for item in numbs:
            if self.check(item) == True:
                final.append(item)
        return final
    def qualified(self, numbs):

        """This returns the fraction of a list that is qualified.

        """
        
        num = len(self.qualify(numbs))
        denom = len(numbs)
        return fractions.Fraction(num, denom)
    def unqualify(self, numbs):
        final = []
        for item in numbs:
            if self.check(item) == False:
                final.append(item)
        return final
    def unqualified(self, numbs):
        num = len(self.unqualify(numbs))
        denom = len(numbs)
        return fractions.Fraction(num, denom)
