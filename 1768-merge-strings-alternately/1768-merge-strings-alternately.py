
class Solution(object):
    def mergeAlternately(self, word1, word2):
        arr = []
        i = 0

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                arr.append(word1[i])

            if i < len(word2):
                arr.append(word2[i])

            i += 1

        return "".join(arr)
