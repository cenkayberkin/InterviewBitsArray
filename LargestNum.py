class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self,A):
        tmpA = []
        for i in A:
            tmpA.append(i)
        A = tmpA
        for i in range(1,len(A)):
            tmp = A[i]
            k = i
            while k > 0 and self.isGreater(tmp,A[k-1]):
                A[k] = A[k - 1]
                k -= 1
            A[k] = tmp

        result =  str("".join([str(i) for i in A]))
        if int(result) == 0:
            return str(0)
        else:
            return result

    def isGreater(self,num1,num2):
        if int(str(num1) + str(num2)) > int(str(num2) + str(num1)):
            return True
        else:
            return False


s = Solution()
print s.largestNumber([0,0])

