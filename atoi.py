__author__ = 'cenk'
import sys

def atoi(text):
    text = text.split()[0].strip()
    isNegative = False

    start = 0
    if text[0] == "-":
        isNegative = True
        start = 1
    elif text[0] == "+":
        start = 1

    t = ""
    for i in range(start,len(text)):
        if text[i] in "0123456789":
            t += text[i]
        else:
            break
    text = t
    result = 0
    pow = 0

    for i in range(len(text))[::-1]:
        result += int(text[i]) * (10 ** pow)
        pow += 1

    if isNegative:
        result = result * -1
        if result < -2147483647:
            return -2147483647
        else:
            return result
    else:
        if result > 2147483647:
            return 2147483647
        else:
            return result
print atoi("5121478262")