__author__ = 'cenk'

def nextPerm(nums):
    pivot = -1
    for i in range(len(nums) -1):
        if nums[i] < nums[i+1]:
            pivot = i

    if pivot == -1:
        # MyReverse(0,nums)
        nums.reverse()
        return

    secondPoint = 0
    for j in range(pivot,len(nums)):
        if nums[j] > nums[pivot]:
            secondPoint = j

    nums[pivot],nums[secondPoint] = nums[secondPoint],nums[pivot]
    for i in range(pivot + 1,(len(nums)+pivot+1)/2):
            nums[i], nums[len(nums) + pivot - i]=nums[len(nums) + pivot - i],nums[i]


a = [3,2,1]
nextPerm(a)
print a