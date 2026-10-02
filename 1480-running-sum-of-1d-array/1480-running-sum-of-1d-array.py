class Solution(object):
    def runningSum(self, nums):
        prefix = [0]
        n = len(nums)
        for i in range(n):
            prefix.append(prefix[i]+nums[i])
        return prefix[1:]
        