__author__ = 'cenk'

def FindDups(nums):
    for i in range(len(nums)):
        if nums[abs(nums[i])] < 0:
            print abs(nums[i])
        nums[abs(nums[i])] = - nums[abs(nums[i])]

print FindDups([4, 2, 4, 5, 2, 3, 1])