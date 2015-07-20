__author__ = 'cenk'


def RadixSort(A):
    location = 1
    digit = 1
    buckets = {}
    tmp = []

    while location <= digit:
        for index,i in enumerate(A):
            if len(str(i)) > digit:
                digit = len(str(i))

            if len(str(i)) < location:
                tmp.append(i)
                continue

            if str(i)[-location] in buckets:
                buckets[str(i)[-location]].append(i)
            else:
                buckets[str(i)[-location]] = [i]

        for i in sorted(buckets.keys()):
            tmp = tmp + buckets[i]
            buckets[i] = []

        A = tmp
        tmp =[]
        location += 1

    maxDiff = 0
    for index in range(0,len(A)):
        if index + 1 != len(A):
            tmp = A[index + 1] - A[index]
            if tmp > maxDiff:
                maxDiff = tmp

    return maxDiff


print RadixSort([43,23,25,0,123,11,3,10,99,1,5,4321])