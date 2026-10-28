
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        low = 0
        total = 0
        res = 0
        freq = {}

        for high in range(len(nums)):
            total += nums[high]
            freq[nums[high]] = freq.get(nums[high], 0) + 1

            if high - low + 1 > k:
                total -= nums[low]
                freq[nums[low]] -= 1

                if freq[nums[low]] == 0:
                    del freq[nums[low]]

                low += 1

            if high - low + 1 == k and len(freq) == k:
                res = max(res, total)

        return res
