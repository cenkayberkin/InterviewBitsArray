__author__ = 'cenk'


def removeDups2(arr):
    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return 1

    i = 0
    j = 0

    while i < len(arr):
        if i + 1 == len(arr):
            if arr[j - 1] != arr[i]:
                arr[j] = arr[i]
                j += 1
            elif arr[j - 1] == arr[i]:
                arr[j] = arr[i]
                j += 1
        elif arr[i] != arr[i + 1]:
            arr[j] = arr[i]
            j += 1
        elif arr[i] == arr[i + 1] and arr[j -1] != arr[i]:
            arr[j] = arr[i]
            j += 1
        i += 1

    if j == 0:
        j = 2
    if j == 1:
        j = 2


    return j

arr = [2,2,2,2]
a = removeDups2(arr)
print arr[:a]


# def removeDups(arr):
#     if len(arr) == 0:
#         return 0
#     if len(arr) == 1:
#         return 1
#
#     i = 0
#     j = 0
#
#     while i < len(arr):
#         if i + 1 == len(arr):
#             if arr[j - 1] != arr[i]:
#                 arr[j] = arr[i]
#                 j += 1
#         elif arr[i] != arr[i + 1]:
#             arr[j] = arr[i]
#             j += 1
#         i += 1
#
#     if j == 0:
#         j = 1
#     return j
#
# arr = []
# a = removeDups(arr)
# print arr[:a]
