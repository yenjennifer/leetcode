class Solution:
    def createTargetArray(self, nums, index):
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i]) #insert(position, element)
        return target

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,0]
    index = [0,1,2,3,0]
    print(s.createTargetArray(nums, index))