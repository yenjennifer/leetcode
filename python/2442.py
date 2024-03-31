nums = [1,13,10,12,31]
# use string to reverse number
class Solution:
    def countDistinctIntegers(self, nums):
        ans = nums.copy()
        for i in nums:
            ans.append(int(str(i)[::-1]))
        return len(set(ans))

## use arithmetic operations to reverse numbers
class Solution:
    def countDistinctIntegers(self, nums):
        nums1 = nums.copy()
        for i in nums:
            reversed_num = 0
            while i != 0:
                current_digit = i % 10 #取餘數
                reversed_num *= 10 #進位
                reversed_num += current_digit
                i = i//10
            nums1.append(reversed_num)
        return len(set(nums1))