__author__ = 'cenk'


def segregateNs(nums):
    j = 0

    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i],nums[j] = nums[j],nums[i]
            j += 1
    return nums


print segregateNs([5,-5,-3,2,-2,10,12,-1])