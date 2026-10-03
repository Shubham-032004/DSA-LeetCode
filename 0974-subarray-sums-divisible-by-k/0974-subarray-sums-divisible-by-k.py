class Solution(object):
    def subarraysDivByK(self, nums, k):

        count = 0
        prefix = 0
        freq = {0: 1}

        for i in range(len(nums)):

            prefix += nums[i]

            remainder = prefix % k

            if remainder in freq:
                count += freq[remainder]

            freq[remainder] = freq.get(remainder, 0) + 1

        return count
        