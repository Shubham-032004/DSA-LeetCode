class Solution(object):
    def maxScore(self, cardPoints, k):
        total = sum(cardPoints)
        n = len(cardPoints)
        window = n - k

        if window == 0:
            return total

        curr = 0
        for i in range(window):
            curr += cardPoints[i]

        min_sum = curr

        for i in range(window, n):
            curr += cardPoints[i] - cardPoints[i - window]
            min_sum = min(min_sum, curr)

        return total - min_sum