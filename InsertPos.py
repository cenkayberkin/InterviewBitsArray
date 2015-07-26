__author__ = 'cenk'


def insertPos(arr,target):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) / 2

        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            if mid == 0:
                return mid
            else:
                hi = mid -1
        elif arr[mid] < target:
            if mid + 1 == len(arr) or arr[mid + 1] > target:
                return mid + 1
            else:
                lo = mid + 1

    return -1

print insertPos([1,3,5,6,7,8,10],2)