__author__ = 'cenk'


# def erdemCount(list, item):
#     if len(list) == 1:
#         if list[0] == item:
#             return 1
#         else:
#             return 0
#
#     m = len(list) / 2
#     return erdemCount(list[0:m],item) + erdemCount(list[m:],item)
#
#
# print erdemCount([1,2,3,4,4,4,4,4,4,5,6],4)


def Count(nums,item):
    start = countEl(nums,item,True)
    end = countEl(nums,item,False)

    if start == -1 and end == -1:
        return 0

    return end - start  +1

def searchRange(A, B):
    sIndex = countEl(A,B,True)
    eIndex = countEl(A,B,False)
    return [sIndex,eIndex]

def countEl(nums,item,firtOccurance):
    start = 0
    end = len(nums) -1
    result = -1

    while start <= end:
        mid = (start + end) /2
        if nums[mid] == item:
            result = mid
            if firtOccurance:
                end = mid - 1
            else:
                start = mid + 1
        elif nums[mid] > item:
            end = mid -1
        elif nums[mid] < item:
            start = mid +1
    return result

print countEl([5, 7, 7, 8, 8, 10],11,True)
# print Count([1,2,3,4,4,4,4,4,5,6,8,10],12)