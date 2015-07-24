__author__ = 'cenk'


def GenMatrix(num):
    size = (num * 2) -1
    matrix = [[0 for x in range(size)] for x in range(size)]
    start = 0
    end = len(matrix)
    top = 0
    bottom = len(matrix)

    direction = 0

    while start <= end:
        if direction == 0:
            for i in range(start,end):
                matrix[top][i] = num
                matrix[bottom - 1][i] = num
            direction = 1
        if direction == 1:
            for i in range(top,bottom):
                matrix[i][start] = num
                matrix[i][end -1] = num
            direction = 0
        num -= 1

        start +=1
        end -= 1
        top += 1
        bottom -=1
    return matrix

a = GenMatrix(1)
for i in a:
    print i