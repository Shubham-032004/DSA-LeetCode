class Solution(object):

    def firstUniqChar(self, s):

        count = {}

        # Character ki frequency count karo
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # First character jiska count 1 hai
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1
        