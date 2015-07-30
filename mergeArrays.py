__author__ = 'cenk'


def merge3(nums1,nums2):
    insertLoc = len(nums1) + len(nums2) - 1

    i = len(nums1) - 1
    j = len(nums2) - 1

    nums1 = nums1 + [0] * len(nums2)
    while insertLoc >= 0:
        if i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[insertLoc] = nums1[i]
                insertLoc -= 1
                i -= 1
            elif nums1[i] < nums2[j]:
                nums1[insertLoc] = nums2[j]
                insertLoc -= 1
                j -= 1
        elif i >= 0 and j <= 0:
            nums1[insertLoc] = nums1[i]
            insertLoc -= 1
            i -= 1
        elif i <= 0 and j >= 0:
            nums1[insertLoc] = nums2[j]
            insertLoc -= 1
            j -= 1
    return nums1

def merge2(nums1, m, nums2, n):
    insertLoc = len(nums1) - 1
    i = m - 1
    j = n - 1

    while insertLoc >= 0:
        if i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[insertLoc] = nums1[i]
                insertLoc -= 1
                i -= 1
            elif nums1[i] < nums2[j]:
                nums1[insertLoc] = nums2[j]
                insertLoc -= 1
                j -= 1
        elif i >= 0 and j <= 0:
            nums1[insertLoc] = nums1[i]
            insertLoc -= 1
            i -= 1
        elif i <= 0 and j >= 0:
            nums1[insertLoc] = nums2[j]
            insertLoc -= 1
            j -= 1


# def merge(nums1, m, nums2, n):
#     insertLoc = len(nums1) - 1
#     i = m - 1
#     j = n - 1
#
#     while i >= 0 and j >= 0:
#         if nums1[i] >= nums2[j]:
#             nums1[insertLoc] = nums1[i]
#             insertLoc -= 1
#             i -= 1
#         elif nums1[i] < nums2[j]:
#             nums1[insertLoc] = nums2[j]
#             insertLoc -= 1
#             j -= 1
#
#     left = 0
#     leftArr = []
#
#     if i == 0:
#         leftArr = nums1
#         left = i
#     else:
#         leftArr  = nums2
#         left = j
#
#     while left >= 0:
#         nums1[insertLoc] = leftArr[left]
#         insertLoc -= 1
#         left -= 1

b = [1,2]
a = [9,13,16,29]
print merge3(a,b)



