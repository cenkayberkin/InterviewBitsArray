__author__ = 'cenk'


def removeEl(arr,item):
    i = 0
    loc = 0
    while i < len(arr):
        if arr[i] != item:
            arr[loc] = arr[i]
            loc += 1
        i += 1
    return loc

a = [8,1,5,2,8,9,8,10,8]
l = removeEl(a,8)
print a[:l]