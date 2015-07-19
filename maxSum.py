__author__ = 'cenk'

def maxset(A):
    max = 0
    curMax = 0

    for index,i in enumerate(A):
        curMax += i
        if curMax > max:
            max = curMax
        elif curMax < 0:
            curMax = 0

    return max

print maxset([5,1,-7,8,-10,1,2,3])



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

