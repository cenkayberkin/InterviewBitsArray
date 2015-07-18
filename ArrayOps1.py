# @param A : tuple of list of integers
# @return a list of integers

def spiralOrder(A):
    result = []
    T = 0
    B = len(A) - 1
    R = len(A[0]) - 1
    L = 0
    direction = 0

    while L <= R and T <= B:
        if direction == 0:
            for i in xrange(L,R + 1):
                result.append(str(A[T][i]))
            T += 1
            direction = 1
        elif direction == 1:
            for i in xrange(T,B + 1):
                result.append(A[i][R])
            R -= 1
            direction = 2
        elif direction == 2:
            for i in (range(L,R + 1)[::-1]):
                result.append(A[B][i])
            B -= 1
            direction = 3
        elif direction == 3:
            for i in (range(T,B + 1)[::-1]):
                result.append(A[i][L])
            L += 1
            direction = 0
    return result

input = [
    [ 1]
]
print spiralOrder(input)


