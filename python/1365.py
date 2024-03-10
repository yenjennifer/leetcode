# class Solution:
#     def smallerNumbersThanCurrent(self, nums):
nums = [8,1,2,2,3]
ans = []
for i in nums:
    count = 0
    for j in nums:
        if i ==j:
            continue
        if i > j:
            count+=1
    ans.append(count)
print(ans)

# if __name__ == '__main__':
#     s = Solution()
#     nums = [8,1,2,2,3]
#     print(s.smallerNumbersThanCurrent(nums))