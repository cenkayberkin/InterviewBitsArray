__author__ = 'cenk'


def searchMatrix2(A,target):
    row = len(A)
    col = len(A[0])
    foundSmallerRow = False

    for i in range(row):
        if A[i][col - 1] >= target:
            row = i
            foundSmallerRow = True
            break

    if not foundSmallerRow:
        return False

    arr = [0] * col

    for i in range(col):
        arr[i] = A [row][i]

    return FindIt(arr,target)


def FindIt(arr, target):
    s = 0
    e = len(arr) - 1

    while s <= e:
        mid = (s + e) /2
        if arr[mid] == target:
            return True
        if arr[mid] > target:
            e = mid -1
        elif arr[mid] < target:
            s = mid + 1
    return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

print searchMatrix2(matrix,3333)

# def searchMatrix(matrix, target):
#     # if len(matrix) == 1 and len(matrix[0]) == 1:
#     #     return matrix[0][0] == target
#
#     startRow = 0
#     startCol = len(matrix[0]) - 1
#
#     while startRow < len(matrix) and startCol >= 0:
#         if target == matrix[startRow][startCol]:
#             return True
#         if target < matrix[startRow][startCol]:
#             startCol -= 1
#         if target > matrix[startRow][startCol]:
#             startRow += 1
#     return False
#
# a = [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#
# a = [[-1]]
# print searchMatrix(a,2)