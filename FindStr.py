__author__ = 'cenk'


def findNeedle(haystack, needle):
    if needle == "" :
        return -1
    if needle == "" and haystack == "":
        return -1
    if len(needle) > len(haystack):
        return -1
    for j in range(len(haystack)):
        if j + len(needle) > len(haystack):
            break
        i = 0
        counter = 0
        k = j
        while haystack[k] == needle[i]:
            if counter == len(needle) - 1:
                return k - counter
            counter += 1
            k += 1
            i += 1

    return -1


h = "ABABRA"
n = "ABRA"
print findNeedle(h,n)