class Solution:
    def leftRightDifference(self, nums):
        nums.insert(0, 0)
        nums.append(0)
        n = len(nums)
        right_sum = []
        left_sum = []
        idx1 = 0
        a = b = 0
        for i in range(n-2):
            a = nums[idx1] + a
            left_sum.append(a)
            idx1 += 1
        idx2 = n-1
        for j in range(n-2):
            b = nums[idx2] + b
            right_sum.append(b)
            idx2 -= 1
        right_sum.reverse()
        ans = []
        for k in range(n-2):
            ans.append(abs((right_sum[k]) - left_sum[k]))
        return (ans)

if __name__ == '__main__':
    s = Solution()
    nums = [10,4,8,3]
    print(s.leftRightDifference(nums))