__author__ = 'cenk'

def buildPascal(level):
    if level <= 0:
        return []

    levels = []
    zero = [1]
    first = [1,1]

    levels.append(zero)
    if level == 1:
        return levels

    levels.append(first)

    for i in range(2,level ):
        width = i + 1
        tmp = [0] * width
        tmp[0] = 1
        tmp[width -1] = 1
        prevLevel = levels[i - 1]
        for i in range(1,width - 1):
            tmp[i] = prevLevel[i -1] + prevLevel[i]
        levels.append(tmp)
    return levels

levels =  buildPascal(1)
for i in levels:
    print i

