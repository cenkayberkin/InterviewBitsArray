__author__ = 'cenk'


def generateIp(text):
    result = []

    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                for l in range(1,4):
                    if i + j + k + l == len(text):
                        r = text[:i] + "." +text[i:i+j] + "."+ text[i + j:i+j+k] + "." +text[i+j+k:i+j+k+l]
                        if isValid(r):
                            result.append(r)
    return result

def isValid(candidate):
    ipAdresses = candidate.split(".")
    for i in ipAdresses:
        if int(i) > 255:
            return False
        if len(i) > 1 and i[0] == '0':
            return False
    return True

# print isValid("001.10.0.1")
print generateIp("010010")
# ["0.10.0.10","0.100.1.0"]