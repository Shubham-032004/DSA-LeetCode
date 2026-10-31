class Solution(object):
    def lengthOfLastWord(self, s):
        ans = s.split()
        return len(ans[-1])
        