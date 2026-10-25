# class Solution(object):
#     def findDisappearedNumbers(self, nums):
#         arr = []

#         for i in range(1, len(nums) + 1):
#             if i not in nums:
#                 arr.append(i)

#         return arr



class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])

        arr = []

        for i in range(len(nums)):
            if nums[i] > 0:
                arr.append(i + 1)

        return arr
        