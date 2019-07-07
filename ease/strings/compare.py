def compare(one, two):
    if len(one) > len(two): numb = len(one)
    else: numb = len(two)
    count = 0
    numbs = []
    start  = None
    end = None
    for x in range(numb):
        if start == None and one[count] == two[count]:
            start = count
        if one[count] != two[count] and start != None:
            numbs.append[start, count]
            start = None
        count += 1
    output = []
    for y in numbs:
        output.append(str(one[y[0]:y[1]]))
    return output
        
#class SimilarData

this = compare("How are your day", "How is your day")
print(this)
