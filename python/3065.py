class Solution:
    def minOperations(self, nums, k):
        return sum(x < k for x in nums)
        # count = 0
        # for x in nums:
        #     if x < k:
        #         count+=1
        # return count

        # nums.sort()
        # for x in nums:
        #     if x >= k:
        #         ans = nums.index(x) 
        #         break
        # return ans

if __name__ == '__main__':
    s = Solution()
    nums = [2,11,10,1,3]
    k = 10
    print(s.minOperations(nums, k))
