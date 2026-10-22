class Solution(object):
    def buildArray(self, nums):
        arr = []
        for i in range(len(nums)):
            i = nums[nums[i]]
            arr.append(i)
        return arr
        