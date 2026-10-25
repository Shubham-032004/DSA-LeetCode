
class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        arr = sorted(freq, key=freq.get, reverse=True)

        return arr[:k]


        