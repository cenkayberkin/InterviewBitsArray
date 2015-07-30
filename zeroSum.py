__author__ = 'cenk'

def isZeroSum(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1,i,-1):
            if i != j and arr[i] + arr[j] == 0:
                return True
            if arr[i] + arr[j] < 0:
                break
    return False

print isZeroSum([-10,-8,-7,-5,1,2,3,4,5,6,9])
