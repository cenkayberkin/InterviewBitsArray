__author__ = 'cenk'


def intersect(A,B):
    result = []

    a = 0
    b = 0

    while a < len(A) and b < len(B):
        if A[a] > B[b]:
            b += 1
        elif A[a] < B[b]:
            a += 1
        elif A[a] == B[b]:
            result.append(A[a])
            a += 1
            b += 1
    return result

A = [1, 2, 3, 3, 4, 5, 6]
B = [3 ,5]
print intersect(A,B)