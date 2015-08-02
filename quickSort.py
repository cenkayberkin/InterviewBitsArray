__author__ = 'cenk'

import random

def quickSelect(arr):
    

print quickSelect([42,7,3,1,10,13,11,22])

def quickSort(arr):
    if len(arr) == 0:
        return []

    less =[]
    more = []
    pivots = []
    pIndex = random.randint(0,len(arr) -1)
    p = arr[pIndex]

    for i in arr:
        if i == p:
            pivots.append(i)
        elif i < p :
            less.append(i)
        else:
            more.append(i)

    return quickSort(less) + pivots + quickSort(more)

# print quickSort([4,3,1,10,11,12])