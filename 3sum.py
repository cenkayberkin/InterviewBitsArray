__author__ = 'cenk'

def twoSum(arr):
    j = len(arr) - 1
    sortedArr = sorted(arr)
    s = set()
    for i in range(len(arr)):
        while j > i:
            if sortedArr[i] + sortedArr[j] < 0:
                break
            if i != j and sortedArr[i] + sortedArr[j] == 0:
                s.add((sortedArr[i],sortedArr[j]))
            j -= 1
    return s

# print twoSum([-10,-8,-5,-1,0,3,5,7,15])

def threesum(arr):
    s = set()
    result = []
    sortedArr = sorted(arr)

    for i in range(len(sortedArr) - 2):
        j = i + 1
        k = len(arr) - 1

        while k > j:
            if sortedArr[j] + sortedArr[k] + sortedArr[i] == 0:
                sortedNums = sorted([sortedArr[i],sortedArr[j],sortedArr[k]])
                s.add(tuple(sortedNums))
                j += 1
                k -= 1
            elif sortedArr[j] + sortedArr[k] +sortedArr[i]< 0:
                j += 1
            else:
                k -= 1

    for i in s:
        result.append([t for t in i])

    return result

print threesum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
