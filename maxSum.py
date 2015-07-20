__author__ = 'cenk'


def maxset(A):
    max = float("-inf")
    maxS = float("-inf")
    maxE = 0

    curMax = 0
    curS = 0

    for index,i in enumerate(A):
        if i >= 0:
            curMax += i
            if curMax > max:
                max = curMax
                maxS = curS
                maxE = index
        else:
            curMax = 0
            curS = index + 1

    if maxS == float("-inf"):
        return []
    else:
        return A[maxS : maxE + 1]

print maxset([ 0, 0, -1, 0 ])



def maxSubArray(A):
    max = 0
    curMax = 0

    for index,i in enumerate(A):
        curMax += i
        if curMax > max:
            max = curMax
        elif curMax < 0:
            curMax = 0

    return max

