__author__ = 'cenk'

import heapq

def reqPainters(A, mid):
    total = 0
    numPainters = 1
    for i in range(len(A)):
        total += A[i]
        if (total > mid):
            total = A[i]
            numPainters += 1
    return numPainters

def paint(A, B, C):
        lo = max(C)
        hi = sum(C)
        n = len(C)

        while lo < hi:
            mid = lo+(hi-lo)/2
            requiredPainters = reqPainters(C, mid)

            if requiredPainters <= A:
                hi = mid
            else:
                lo = mid + 1
        return B*lo%10000003

print paint(3,10,[ 640, 435, 647, 352, 8, 90, 960, 329, 859 ])

# def FindMinTime(numPainter,timeForUnit, tasks):
#     tasks= sorted(tasks,reverse=True)
#     painters = [0] * numPainter
#     heapq.heapify(painters)
#
#     for i in tasks:
#         tmp = heapq.heappop(painters)
#         tmp += i
#         heapq.heappush(painters,tmp)
#     print heapq.nlargest(1,painters)[0] * timeForUnit
#

# FindMinTime(3,10,[ 640, 435, 647, 352, 8, 90, 960, 329, 859 ])
# 9140 cevap