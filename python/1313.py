class Solution:
    def decompressRLElist(self, nums):
        arr = []
        for i in range(len(nums)//2):
            arr += [nums[2*i+1]]*nums[2*i]
        return arr

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4]
    print(s.decompressRLElist(nums)) 