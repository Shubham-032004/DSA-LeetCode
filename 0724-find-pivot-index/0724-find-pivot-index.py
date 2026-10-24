# class Solution(object):
#     def pivotIndex(self, nums):
        # prefix = [0]
        # for i in range(len(nums)):
        #     prefix.append(prefix[i]+nums[i])
        # for i in range(len(nums)):
        #     left_sum = prefix[i]
        #     right_sum = prefix[-1] - prefix[i+1]
        #     if left_sum == right_sum:
        #         return i
        # return -1
       

class Solution(object):
    def pivotIndex(self, nums):
        left = 0
        total = sum(nums)

        for i in range(0, len(nums)):
            right = total - left - nums[i]

            if left == right:
                return i

            left += nums[i]

        return -1


        