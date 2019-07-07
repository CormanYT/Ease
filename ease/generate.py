import string, random

def a():
    return "A"
function = type(a)
_class = type(function)

class This:
    pass

a = This
for x in range(5):
    a = type(a)
    print(a)

def generate(instance=str, *args):
    length = args[0]
    global function
    global _class
    if instance == _class or instance == "class" or instance == "type":
        class new:
            for name, value in length.items():
                exec("{} = value".format(name))
        return new
    if instance == function or instance == "function":
        def new(*args, **kwargs):
            for x in length.splitlines():
                exec(x)
        return new
    if instance == str:
        letters = string.ascii_letters + string.digits + string.punctuation
        output = []
        for x in range(length):
            output.append(random.choice(letters))
        return "".join(output)        
    if instance == int:
        this = "0" * (length - 1)
        that = "9" * length
        e = "1" + this
        return random.randint(int(e), int(that))
    if instance == float:
        declength = args[1]
        one = str(generate(int, length))
        two = str(generate(int, declength))
        final = one + "." + two
        return float(final)
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

this = generate(function, "print('Hi')")
this()
this()
this()
