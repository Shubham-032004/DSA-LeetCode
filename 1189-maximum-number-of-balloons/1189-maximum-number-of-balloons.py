class Solution(object):

    def maxNumberOfBalloons(self, text):

        freq = {}

        for ch in text:
            freq[ch] = freq.get(ch, 0) + 1

        b = freq.get('b', 0)
        a = freq.get('a', 0)
        l = freq.get('l', 0) // 2
        o = freq.get('o', 0) // 2
        n = freq.get('n', 0)

        return min(b, a, l, o, n)
        
        