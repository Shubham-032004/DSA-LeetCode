class Solution(object):
    def findMiddleIndex(self, nums):
        left = 0
        total = sum(nums)
        for i in range(0,len(nums)):
            right = total-left-nums[i]
            if right == left:
                return i
            left += nums[i]
        return -1        