__author__ = 'cenk'

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def insert(intervals, newInterval):
    intervals.append(newInterval)
    return mergeIntervals(intervals)

def mergeIntervals(intervals):

    if len(intervals) == 0:
        return []
    arr = sorted(intervals,key=lambda tup: tup.start)
    i = 0
    while i < len(arr) - 1:
        if arr[i].end >= arr[i +1].start:
            arr[i + 1].start = arr[i].start
            arr[i + 1].end = max(arr[i + 1].end,arr[i].end)
            arr[i].start = -1
            arr[i].end = -1
        i +=1
    r = [i for i in arr if i.start != -1]
    print [str(i.start) + " " + str(i.end) for i in r]
    return r

i1 = Interval(1,2)
i2 = Interval(3,5)
i3 = Interval(6,7)
i4 = Interval(8,10)
i5 = Interval(12,16)

newInterval = Interval(4,9)
intervals = [i1,i2,i3,i4,i5]
print insert(intervals,newInterval)
# print mergeIntervals(intervals)


