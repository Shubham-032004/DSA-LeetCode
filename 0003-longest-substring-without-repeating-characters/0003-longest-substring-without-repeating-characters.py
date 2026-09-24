# class Solution(object):
#     def lengthOfLongestSubstring(self, s):

#         left = 0
#         chars = set()
#         max_len = 0

#         for right in range(len(s)):

#             while s[right] in chars:
#                 chars.remove(s[left])
#                 left += 1

#             chars.add(s[right])

#             max_len = max(max_len, right - left + 1)

#         return max_len


class Solution(object):
    def lengthOfLongestSubstring(self, s):

        freq = {}
        left = 0
        max_len = 0

        for right in range(len(s)):

            freq[s[right]] = freq.get(s[right], 0) + 1

            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len