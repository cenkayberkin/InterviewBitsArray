__author__ = 'cenk'


def mostWater(arr):
    maxWater = 0
    left = 0
    right = len(arr) - 1

    while left < right:
        minSide = min(arr[left],arr[right])
        bottom = right - left
        maxWater = max(maxWater,minSide * bottom)
        if arr[left] > arr[right]:
            right -= 1
        elif arr[left] <= arr[right]:
            left += 1
    return maxWater

print mostWater([1,3,2,1,4,2])