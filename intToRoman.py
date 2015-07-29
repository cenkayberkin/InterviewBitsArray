__author__ = 'cenk'


def intToRoman(num):
    alph = "MDCLXVI"
    alphDict = { 'M':1000, 'D':500, 'C':100, 'L': 50,'X':10,'V':5,'I':1}
    numDict = { 1000:'M', 500:'D', 100:'C', 50:'L',10:'X',5:'V',1:'I'}
    result = ""

    while num > 0:
        for index,i in enumerate(alph):
            roman = alphDict[i]
            if num >= roman:
                pre = num / roman
                num = num % roman
                newNum = numDict[roman] * pre
                result += newNum
            for j in range(index+1,len(alph)):
                next = alphDict[alph[j]]
                if next * 2 != roman:
                    if roman - next <= num < roman:
                        result += numDict[next] + numDict[roman]
                        num = num % (roman - next)
    return result

print intToRoman(9)