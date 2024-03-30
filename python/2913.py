nums = [1,2,1]
##O(N^2), O(N)
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

##O(N^3), O(N^2)
class Solution:
    def sumCounts(self, nums) -> int:
        sum = 0
        for i in range(len(nums)):
            set1 = set()
            for j in range(i,len(nums)):
                set1.add(nums[j])
                sum+=len(set1)**2
        return sum

        # sum = 0
        # sum+=len(nums)
        # for i in range(len(nums)):
        #     for j in range(i+2,len(nums)+1):
        #         sum += len(set(nums[i:j]))**2 ##has to create a set in nested loops
        # return sum