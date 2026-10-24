
class Solution(object):
    def checkSubarraySum(self, nums, k):
        total = 0
        freq = {0: -1}

        for i in range(len(nums)):
            total += nums[i]
            rem = total % k

            if rem in freq:
                if i - freq[rem] >= 2:
                    return True
            else:
                freq[rem] = i

        return False

                
        