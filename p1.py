
A = [ 14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77, 35 ]
B = 56
ret = []

for i in xrange(len(A)):
    location = (i + B) % (len(A))
    ret.append(A[location])
print ret