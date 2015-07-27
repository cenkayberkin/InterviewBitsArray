__author__ = 'cenk'


def countAndSay(num):
    if num == 1:
        return 1

    result = "1"

    for i in range(num -1):
        result = readAndGenerate(str(result))
    return str(result)

def readAndGenerate(text):
    if len(text) == 1:
        return "1" + text[0]
    i = 0
    result = ""
    cur = 1

    while i < len(text) - 1:
        if i+ 1 == len(text)-1:
            if text[i] != text[i +1]:
                result += str(cur) + text[i]
                cur = 1
                result += str(cur) + text[i + 1]
            elif text[i] == text[i +1]:
                cur += 1
                result += str(cur) + text[i]
        elif text[i] != text[i +1]:
            result += str(cur) + text[i]
            cur = 1
        elif text[i] == text[i +1]:
            cur += 1
        i += 1

    return result

print countAndSay(2)