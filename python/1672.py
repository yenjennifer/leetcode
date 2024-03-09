class Solution:
    def maximumWealth(self, accounts):
        wealth = []
        for i in accounts:
            sum1 = sum(i)
            wealth.append(sum1)
        return max(wealth)