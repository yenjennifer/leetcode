class Solution:
    def differenceOfSum(self, nums):
        sum1 = sum2 = 0
        for x in nums:
            sum1 += x
            for y in str(x):
                sum2 +=int(y)
        return abs(sum1-sum2)
        