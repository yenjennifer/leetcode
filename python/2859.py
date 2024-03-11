class Solution:
    def sumIndicesWithKSetBits(self, nums, k):
        ans = []
        for i in range(len(nums)):
            a = bin(i)
            if a.count("1") == k:
                ans.append(nums[i])
        return sum(ans)


if __name__ == '__main__':
    s = Solution()
    nums = [5,10,1,5,2]
    k = 1
    print(s.sumIndicesWithKSetBits(nums, k))