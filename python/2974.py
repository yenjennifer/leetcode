class Solution:
    def numberGame(self, nums):
        nums1 = sorted(nums)
        rounds = len(nums1)//2
        i = 0
        arr = []
        for _ in range(rounds):
            arr.append(nums1[i+1])
            arr.append(nums1[i])
            i += 2
        return arr


if __name__ == '__main__':
    s = Solution()  
    nums = [5,4,2,3]
    print(s.numberGame(nums))
        