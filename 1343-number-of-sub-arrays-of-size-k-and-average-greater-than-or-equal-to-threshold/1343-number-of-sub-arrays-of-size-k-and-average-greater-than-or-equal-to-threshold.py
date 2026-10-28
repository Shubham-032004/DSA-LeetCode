class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        low = 0
        high = k - 1
        count = 0
        total = 0

        for i in range(k):
            total += arr[i]

        if total / float(k) >= threshold:
            count += 1

        while high < len(arr) - 1:
            total = total - arr[low]
            low += 1
            high += 1
            total = total + arr[high]

            avg = total / float(k)

            if avg >= threshold:
                count += 1

        return count