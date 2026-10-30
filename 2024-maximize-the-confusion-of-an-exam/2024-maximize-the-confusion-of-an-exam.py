class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        low = 0
        count_T = 0
        count_F = 0
        ans = 0

        for high in range(len(answerKey)):
            if answerKey[high] == 'T':
                count_T += 1
            else:
                count_F += 1

            while (high - low + 1) - max(count_T, count_F) > k:
                if answerKey[low] == 'T':
                    count_T -= 1
                else:
                    count_F -= 1

                low += 1

            ans = max(ans, high - low + 1)

        return ans
        