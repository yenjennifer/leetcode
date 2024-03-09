class Solution:
    def countPairs(self, nums, target):
        count = 0
        ptr1 = 1
        for i in nums:
            for j in nums[ptr1:]:
                #print([i,j])
                if i + j < target:
                    count +=1
            ptr1+=1
        return count

if __name__ == '__main__':
    s = Solution()
    nums = [-6,2,5,-2,-7,-1,3]
    target = -2
    print(s.countPairs(nums, target))