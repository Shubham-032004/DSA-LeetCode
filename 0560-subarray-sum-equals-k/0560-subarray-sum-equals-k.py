class Solution(object):
    def subarraySum(self, nums, k):

        prefix = 0
        count = 0
        freq = {0: 1}

        for i in range(len(nums)):

            prefix += nums[i]

            previous_sum = prefix - k

            if previous_sum in freq:
                count += freq[previous_sum]

            freq[prefix] = freq.get(prefix, 0) + 1

        return count

        