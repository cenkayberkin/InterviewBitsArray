__author__ = 'cenk'

def validPalindrom(text):
    if len(text) <= 1:
        return True

    cleanText = [i.upper() for i in text if i.isalnum()]
    for i in range(len(cleanText) / 2):
        if cleanText[i] != cleanText[-(1+i)]:
            return False
    return True

print validPalindrom("race a car")