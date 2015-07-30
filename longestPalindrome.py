__author__ = 'cenk'

def longestPalindrome(s):
    n = len(s)

    if n == 0:
        return ""

    table = [[False for x in range(1000)] for x in range(1000)]
    maxst = 0
    maxlen = 1

    for i in range(n):
        table[i][i] = True
        maxst = i
        maxlen = 1

    for i in range(n-1):
        if s[i]==s[i+1]:
            table[i][i+1]= True
            maxst = i
            maxlen = 2

    for length in range(3,n + 1):
        for i in range(n-length+1):
            j= i+ length-1
            if s[i]==s[j] and table[i+1][j-1]:
                table[i][j]=True
                maxst = i
                maxlen = length

    return s[maxst:maxlen]

print longestPalindrome("abac")