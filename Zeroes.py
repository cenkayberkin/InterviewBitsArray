__author__ = 'cenk'

def setZeroes(matrix):
    numRows = len(matrix)
    numCols = len(matrix[0])
    fColHasZero = False
    fRowHasZero = False

    for col in range(0,numCols):
        if matrix[0][col] == 0:
            fRowHasZero = True
            break

    for row in range(0,numRows):
        if matrix[row][0] == 0:
            fColHasZero = True
            break

    for row in range(1,numRows):
        for col in range(1,numCols):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

    # Fill col with zero
    for col in range(1,numCols):
        if matrix[0][col] == 0:
            for i in range(1,numRows):
                matrix[i][col] = 0

    # Fill row with zero
    for row in range(1,numRows):
        if matrix[row][0] == 0:
            for i in range(1,numCols):
                matrix[row][i] = 0

    if fColHasZero:
        for row in range(0,numRows):
            matrix[row][0] = 0

    if fRowHasZero:
        for col in range(0,numCols):
            matrix[0][col] = 0



matrix  = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
result = setZeroes(matrix)
print matrix