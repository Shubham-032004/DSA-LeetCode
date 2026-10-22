# class Solution(object):
#     def runningSum(self, nums):
#         prefix = [0]
#         n = len(nums)
#         for i in range(n):
#             prefix.append(prefix[i]+nums[i])
#         return prefix[1:]

class Solution(object):
    def runningSum(self, nums):
        arr = []
        sum = 0
        for i in range(0,len(nums)):
            sum = sum + nums[i]
            arr.append(sum)
        return arr
        