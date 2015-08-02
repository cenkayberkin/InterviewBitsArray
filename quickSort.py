__author__ = 'cenk'

import random

def findKthLargest(arr,k):
    if len(arr) == 1:
        return arr[0]
    kthSmallest = len(arr) - k + 1
    return findKthSmallest(arr,kthSmallest)

def findKthSmallest(arr,k):
    less =[]
    more = []
    pIndex = random.randint(0,len(arr) -1)
    p = arr[pIndex]
    pivots = []

    for i in arr:
        if i == p:
            pivots.append(i)
        elif i < p :
            less.append(i)
        else:
            more.append(i)

    if k <= len(less):
        return findKthSmallest(less,k)
    elif k > len(less) + len(pivots):
        return findKthSmallest(more,k - (len(less) + len(pivots)))
    else:
        return p

print findKthLargest([3,2,1,5,6,4],2)


# def quickSelect(arr,k):
#     less =[]
#     more = []
#     pIndex = random.randint(0,len(arr) -1)
#     p = arr[pIndex]
#     pivots = []
#
#     for i in arr:
#         if i == p:
#             pivots.append(i)
#         elif i < p :
#             less.append(i)
#         else:
#             more.append(i)
#
#     if k <= len(less):
#         return quickSelect(less,k)
#     elif k > len(less) + len(pivots):
#         return quickSelect(more,k - (len(less) + len(pivots)))
#     else:
#         return p
#
# print quickSelect([3,2,1,5,6,4],2)



# def quickSort(arr):
#     if len(arr) == 0:
#         return []
#
#     less =[]
#     more = []
#     pivots = []
#     pIndex = random.randint(0,len(arr) -1)
#     p = arr[pIndex]
#
#     for i in arr:
#         if i == p:
#             pivots.append(i)
#         elif i < p :
#             less.append(i)
#         else:
#             more.append(i)
#
#     return quickSort(less) + pivots + quickSort(more)

# print quickSort([4,3,1,10,11,12])