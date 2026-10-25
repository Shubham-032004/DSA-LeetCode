class Solution(object):
    def convertToTitle(self, columnNumber):
        result = ""

        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            result = chr(rem + ord('A')) + result
            columnNumber //= 26

        return result
        