
class Solution(object):
    def isHappy(self, n):
        while n != 1 and n != 4:
            res = 0

            while n > 0:
                num = n % 10
                res += num ** 2
                n = n // 10

            n = res

        return n == 1

        