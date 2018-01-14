'''
Subset of Sums
Logic - Two options for recursion , either you add or neglect the number in the set
Question - Find out the number of sets that can sum up to a given target value
- Use recursion first
- To make it faster we do memoization

Eg:
nums=[2,4,6,10,12], target = 20 , sets = {2,6,12}, {4,6,10} , Ans: 2
'''

class Solution(object):
    def __init__(self):
        super(Solution, self).__init__()

    def subsetcount(self, nums, target):
        memo={}
        #return self.rec(nums, target, len(nums)-1)
        return self.dp(nums, target, len(nums)-1, memo)

    def rec(self,nums, t, i):
        if t==0:return 1
        if not nums:return 0
        if t<0: return 0
        if i<0:return 0
        if t<nums[i]: return self.rec(nums, t, i-1)
        else:
            return self.rec(nums, t, i-1) + self.rec(nums, t-nums[i], i-1) # Either do not add(neglect) or add

    def dp(self, nums, t, i ,mem):
        key=str(t)+":"+str(i)
        if key in mem:
            return mem[key]
        else:
            if t==0:return 1
            if not nums:return 0
            if t<0: return 0
            if i<0:return 0
            if t<nums[i]:
                to_ret= self.dp(nums, t, i-1, mem)
            else:
                to_ret=self.dp(nums, t-nums[i], i-1, mem) + self.dp(nums, t, i-1, mem)
            mem[key]=to_ret
            return to_ret


obj=Solution()
nums=[2,4,6,10,12]
target=16
print(obj.subsetcount(nums,target))
