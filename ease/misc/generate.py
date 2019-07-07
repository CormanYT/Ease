import string, random

def generate(instance=str, length=0):
    if instance == str:
        letters = string.ascii_letters + string.digits + string.punctuation
        output = []
        for x in range(length):
            output.append(random.choice(letters))
        return "".join(output)
        
    if instance == int:
        this = "0" * (length - 1)
        that = "9" * length
        return random.randint(int("1" + this), int(that))
    if instance == bool:
        return random.choice([True, False])
    if instance == list:
        this = []
        types = [str, int, bool]
        for x in range(length):
            this.append(generate(random.choice(types), 1))
        return this
    else:
        raise ValueError('Generate does not support a ' + str(length))
