__author__ = 'cenk'


def sqrt(num):
    if num == 0:
        return 0
    if num < 4 and num >0:
        return 1

    start = 0
    end = num - 1

    while start <= end:
        mid = (start + end) / 2

        if mid ** 2 == num or mid ** 2 < num < (mid+1) ** 2:
            return mid
        elif mid ** 2 > num:
            end = mid -1
        elif mid ** 2 < num:
            start = mid + 1

print sqrt(4)