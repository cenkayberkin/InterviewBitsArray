__author__ = 'cenk'

# 00000010100101000001111010011100
def reverseBits(num):
    result = 0
    mask = 1

    for i in range(0,32):
        if num & mask != 0:
            result += 1
        if i != 31:
            result = result << 1
        mask = mask << 1

    return result

print reverseBits(43261596)

# def singleNumber(arr):
#     i = 1
#     result = arr[0]
#     while i < len(arr):
#         result = result ^ arr[i]
#         i += 1
#     return result
#
# print singleNumber([4,2,3,2,5,3,4])

# def numOfOnebits(num):
#     if num == 0:
#         return 0
#     count = 0
#     while num > 0:
#         if (num & 1) == 1:
#             count += 1
#         num = num >> 1
#     return count
#
# print numOfOnebits(19)