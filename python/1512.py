class Solution:
    def numIdenticalPairs(self, nums):
        count = 0
        nums1 = nums.copy()
        #i,j is elements in nums
        for i in nums:
            nums1.pop(0)
            for j in nums1:
                if i == j:
                    count +=1
        return count