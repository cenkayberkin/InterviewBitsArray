__author__ = 'cenk'


def Pow(base,exp):
    fbase = float(base)

    if exp < 0:
        fbase = 1 / float(base)
        exp = abs(exp)

    if fbase == 0:
        return 0
    if exp == 0:
        return 1

    processList = []
    while exp > 1:
        if exp % 2 == 1:
            exp -= 1
            processList.append(1)
        else:
            exp /= 2
            processList.append(0)

    reversedProcessList = processList[::-1]

    result = fbase
    for i in reversedProcessList:
        if i == 0:
            result = result ** 2

        else:
            result = result * fbase


    return result

print "%.8f" % Pow(34.00515,-3)