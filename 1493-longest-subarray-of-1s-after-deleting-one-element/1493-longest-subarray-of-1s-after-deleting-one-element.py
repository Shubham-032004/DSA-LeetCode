class Solution(object):
    def longestSubarray(self, nums):
        low = 0
        count = 0
        max_len = 0

        for high in range(len(nums)):
            if nums[high] == 0:
                count += 1

            while count > 1:
                if nums[low] == 0:
                    count -= 1
                low += 1

            max_len = max(max_len, high - low)

        return max_len



                

        
        