class Solution:
    def arithmeticTriplets(self, nums, diff):
        s1 = set(nums)
        count = 0
        for i in nums:
            if i+diff in s1 and i+2*diff in s1:
                count+=1
        return count