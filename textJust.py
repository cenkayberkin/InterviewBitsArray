__author__ = 'cenk'


def fullJustify(words, maxWidth):
    if maxWidth == 0:
        return [""]
    result = []

    i = 0
    tmp = ""
    tmpSize = 0
    numOftmpWord = 0
    space = 0
    while i < len(words):

        if len(words[i]) + tmpSize + space <= maxWidth:
            tmpSize += len(words[i]) + space
            numOftmpWord += 1
            tmp += words[i] + " "
            if i + 1 == len(words):
                result.append(tmp)
        elif len(words[i]) == maxWidth:
            if tmp != "":
                result.append(tmp)
            tmpSize = len(words[i])
            tmp = words[i]
            numOftmpWord = 1
            if i + 1 == len(words):
                result.append(tmp)
        else:
            if tmp != "":
                result.append(tmp)
                numOftmpWord  = 0

            tmpSize = len(words[i]) + 1
            tmp = words[i] + " "
            numOftmpWord = 1
            if i + 1 == len(words):
                result.append(tmp)
        space = numOftmpWord - 1
        i += 1

    j = 0
    while j < len(result):
        if j + 1 != len(result):
            result[j] = insertPaddings(result[j],maxWidth,False)
        else:
            result[j] = insertPaddings(result[j],maxWidth,True)
        j += 1

    return result

def insertPaddings(text,size,lastRow):

    words = text.split()

    if len(words) == 0:
        return " " * size

    sumOfChars = 0
    numWords = len(words)

    for i in words:
        sumOfChars += len(i)
    high = 0
    low = 0

    emptyChars = size  - sumOfChars

    if lastRow:
        result = ""
        count = len(words) -1
        for i in words:
            result += i + " "
        result = result.rstrip() + " " * (size - sumOfChars - count)
        return result
    elif numWords > 1:
        low = emptyChars / (numWords - 1)
        high = low + 1
        numOfHigh = emptyChars % (numWords - 1)
    else:
        return  words[0] + " " * (size - sumOfChars)

    numOfLow = numWords - 1 - numOfHigh
    result = ""
    for index,i in enumerate(words):
        if numOfHigh > 0:
            result += i + " " * high
            numOfHigh -= 1
        else:
            if index == len(words) -1:
                result += i
            else:
                result += i + " " * low
    return result

# w = ""

# print insertPaddings(w,14)

words = ["Listen","to","many,","speak","to","a","few."]
L = 6
# ['Listen', 'to    ', 'many, ', 'speak ', 'to   a', 'few.  ']
# ["Listen","to    ","many, ","speak ","to   a","few.  "]
# words = ["What","must","be","shall","be."]
# L = 12
print fullJustify(words,L)