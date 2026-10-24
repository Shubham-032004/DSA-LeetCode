class Solution(object):
    def findMaxLength(self, nums):
        freq = {0: -1}
        total = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                total -= 1
            else:
                total += 1

            if total in freq:
                max_len = max(max_len, i - freq[total])
            else:
                freq[total] = i

        return max_len
        