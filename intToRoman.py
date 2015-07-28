__author__ = 'cenk'


def intToRoman(num):
    alph = "MDCLXVI"
    alphDict = { 'M':1000, 'D':500, 'C':100, 'L': 50,'X':10,'V':5,'I':1}
    numDict = { 1000:'M', 500:'D', 100:'C', 50:'L',10:'X',5:'V',1:'I'}
    result = ""

    while num > 0:
        for i in alph:
            roman = alphDict[i]
            if num >= roman:
                pre = num / roman
                num = num % roman
                newNum = numDict[roman] * pre
                result += newNum
    return result

print intToRoman(160)