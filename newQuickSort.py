__author__ = 'cenk'

from random import *

def Shuffle(arr):
    for i in range(len(arr)):
        randIndex = randint(0,i)
        tmp = arr[randIndex]
        arr[randIndex] = arr[i]
        arr[i] = tmp

def quickSort(arr):
    Shuffle(a)
    print a
    quickSortHelper(arr,0,len(arr)-1)

def quickSortHelper(arr,first,last):
    if first < last:
        partIndex = partition(arr,first,last)
        quickSortHelper(arr,first,partIndex - 1)
        quickSortHelper(arr,partIndex + 1,last)

def partition(arr,left,right):

    pivotIndex = left
    pivotValue = arr[left]
    left = left + 1
    right = right

    done = False

    while not done:
        while left <= right and arr[left] <= pivotValue:
            left += 1
        while left <= right and pivotValue <= arr[right]:
            right -= 1

        if right < left :
            done = True
        else:
            tmp = arr[right]
            arr[right] = arr[left]
            arr[left] = tmp

    tmp = arr[right]
    arr[right] = arr[pivotIndex]
    arr[pivotIndex] = tmp
    return right

# a = [54,26,93,17,77,31,44,55,20]
a = [20, 31, 54, 26, 17, 55, 44, 93, 77]
quickSort(a)
print a

