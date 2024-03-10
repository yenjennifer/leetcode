class Solution:
    def runningSum(self, nums):
       running_sums = []
       current_sum = 0
       for i in nums:
           current_sum = current_sum + i
           running_sums.append(current_sum)
       return running_sums 



if __name__ == '__main__':
    s = Solution()
    nums = [3,1,2,10,1]
    print(s.runningSum(nums))