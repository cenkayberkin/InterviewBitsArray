__author__ = 'cenk'

def firstMissingPositive(A):
    j = 0
    n = len(A)
    for i in range(n):
        if A[i] <= 0:
            A[i],A[j] = A[j],A[i]
            j+=1
    for i in range(j,n):
        if abs(A[i])-1+j < n and A[abs(A[i])-1+j] > 0:
            A[abs(A[i])-1+j] = -A[abs(A[i])-1+j]

    for i in range(j,n):
        if A[i] > 0:
            return i-j+1
    return n - j + 1

print firstMissingPositive([2, 3, -7, 6, 8, 1, -10, 15])