__author__ = 'cenk'

def threesum(arr):
    i = 0
    s = set()
    result = []

    while i < len(arr):
        j = i + 1
        while j < len(arr):
            k = j + 1
            while k < len(arr):
                if arr[i] + arr[j] + arr[k] == 0:
                    sortedNums = sorted([arr[i],arr[j],arr[k]])
                    s.add(tuple(sortedNums))
                k += 1
            j += 1
        i += 1

    for i in s:
        result.append([t for t in i])

    return result

print threesum([-1 ,0 ,1 ,2 ,-1 ,-4])
