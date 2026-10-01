class Solution(object):
    def maxAbsoluteSum(self, nums):
        max_current = nums[0]
        max_sum = nums[0]

        min_current = nums[0]
        min_sum = nums[0]

        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            max_sum = max(max_sum, max_current)

            min_current = min(nums[i], min_current + nums[i])
            min_sum = min(min_sum, min_current)

        return max(max_sum, abs(min_sum))
        