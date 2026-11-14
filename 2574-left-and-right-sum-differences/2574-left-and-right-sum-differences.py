class Solution(object):
    def leftRightDifference(self, nums):
        total = sum(nums)
        leftSum = 0
        ans = []

        for i in range(len(nums)):

            rightSum = total - leftSum - nums[i]

            difference = abs(leftSum - rightSum)

            ans.append(difference)

            leftSum += nums[i]

        return ans