__author__ = 'cenk'

def partialReverse(arr,lo,hi):
    length = hi -lo
    step = length
    i = lo

    while step > 1:
        tmp = arr[i + step]
        arr[i + step] = arr[i]
        arr[i] = tmp
        i +=1
        step -= 2

def reverse(arr):
    for i in range(len(arr)/2):
        tmp = arr[-(i +1)]
        arr[-(i +1)] = arr[i]
        arr[i] = tmp

a = [1,2,3,4,5,6,7,8,9]
partialReverse(a,0,4)
print a