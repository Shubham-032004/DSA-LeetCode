
class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0

        for i in range(len(accounts)):
            total = sum(accounts[i])

            if total > max_wealth:
                max_wealth = total

        return max_wealth

        