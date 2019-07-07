def shared(one, two):
    three = []
    for item in one:
        if item in two:
            three.append(item)
    return three
