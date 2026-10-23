
class Solution(object):
    def maxVowels(self, s, k):
        low = 0
        count = 0
        max_str = 0
        vowels = "aeiou"

        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_str = count

        for high in range(k, len(s)):
            if s[high] in vowels:
                count += 1

            if s[low] in vowels:
                count -= 1

            low += 1
            max_str = max(max_str, count)

        return max_str


        