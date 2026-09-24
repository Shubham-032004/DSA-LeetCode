class Solution(object):
    def totalFruit(self, fruits):
        low = 0
        freq = {}
        max_len = 0

        for high in range(len(fruits)):

            freq[fruits[high]] = freq.get(fruits[high], 0) + 1

            while len(freq) > 2:
                freq[fruits[low]] -= 1

                if freq[fruits[low]] == 0:
                    del freq[fruits[low]]

                low += 1

            max_len = max(max_len, high - low + 1)

        return max_len