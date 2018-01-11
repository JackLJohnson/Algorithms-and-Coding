# Trying in Python
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
import re
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print("chek-1", nums, target)
        listret = []

        if (sum(nums) == target):
            for val in range(0, len(nums)):
                listret.append(val)
        elif (sum(nums) > target):
            for idx,val in enumerate(nums):
                for j in range(1, len(nums)):
                    if (val+nums[j] == target):
                        return([idx,j])
        elif (sum(nums) < target):
            return 0

    def __init__(self):
        super(Solution, self).__init__()
        nums = [2,7,11,15]
        target = 9
        print("The indices",self.twoSum(nums, target))

x = Solution()
