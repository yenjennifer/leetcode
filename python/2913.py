nums = [1,2,1]
##optimzed, beats 100%##
class Solution:
    def sumCounts(self, nums) -> int:
        sum = 0
        set1 = set()
        for i in range(len(nums)):
            sub = 0
            for j in range(i,len(nums)):
                if j not in set1:
                    set1.add(nums[j])
                sub+=len(set1)**2
            sum+=sub
            set1.clear()
        return sum

        # sum = 0
        # sum+=len(nums)
        # for i in range(len(nums)):
        #     for j in range(i+2,len(nums)+1):
        #         sum += len(set(nums[i:j]))**2 ##has to create a set in nested loops
        # return sum