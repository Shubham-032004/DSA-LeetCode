class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        freq = {}
        for i in magazine:
            freq[i] = freq.get(i,0) + 1
        for j in ransomNote:
            if j not in freq or freq[j]==0:
                return False
            freq[j] -= 1
        return True
        