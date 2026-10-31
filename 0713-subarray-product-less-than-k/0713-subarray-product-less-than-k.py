class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        low = 0
        total = 1
        count = 0

        for high in range(len(nums)):
            total *= nums[high]

            while total >= k and low <= high:
                total //= nums[low]
                low += 1

            count += high - low + 1

        return count


        