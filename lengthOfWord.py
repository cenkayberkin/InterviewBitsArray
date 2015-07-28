__author__ = 'cenk'

def lengthLastWord(text):
    if len(text) == 0:
        return 0
    word = ""
    text = text.rstrip()
    for i in range(len(text)):
        if text[- (i + 1)].isalpha():
            word += text[- (i + 1)]
        if word != "" and not text[- (i + 1)].isalpha():
            break
    return len(word)

# print lengthLastWord("benim adim 2  sds cenkss 2  ")