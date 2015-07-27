__author__ = 'cenk'


def LCP(arr):
    if len(arr) == 0:
        return ""
    if len(arr) == 1:
        return arr[0]

    length = len(arr)
    index = 0
    minText = min(arr)

    max =  min([len(i) for i in arr])

    done = False

    while index < max:
        for i in range(len(arr) - 1):
            if arr[i][index] != arr[i + 1][index]:
                done = True
                break
        if done:
            return minText[:index]
        else:
            index += 1

    return minText[:index]

print LCP([

  "abcdefgh",

  "aefghijk",

  "abcefgh"
])
