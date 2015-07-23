__author__ = 'cenk'

def plusOne(A):
    remainder = 0

    for i in range(0,len(A))[::-1]:
        if i == (len(A) -1):
            remainder = 1
        if A[i] + remainder > 9:
            remainder = 1
            A[i] = 0
        else:
            A[i] = A[i] + remainder
            remainder = 0

    if remainder == 1:
        result = [1]
        result = result + A
        return result
    else:
        nonZeroS = 0
        for index,i in enumerate(A):
            if i != 0:
                nonZeroS = index
                break
        return A[nonZeroS:]
print plusOne([0,1, 9, 9, 9, 9 ])