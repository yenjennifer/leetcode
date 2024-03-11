class Solution:
    def smallerNumbersThanCurrent(self, nums):
        # sort the list, the order of the list(index) = the amount of elements it is larger than
        # [8,1,2,2,3] --> [1,2,2,3,8]
        #           index |0|1|2|3|4|
        # index of 8 is |4|, which is greater than the 4 elements in front of it.
        # index of 2 is |1|,|2|, we only have to get the first index, which is |1|, and 2 is only greater than 1 of the elements
        ans = []
        sorted_nums = sorted(nums)
        for x in nums:
            a = sorted_nums.index(x)
            ans.append(a)
        return ans
    
        # ans = []
        # for i in nums:
        #     count = 0
        #     for j in nums:
        #         if i ==j:
        #             continue
        #         if i > j:
        #             count+=1
        #     ans.append(count)
        # return(ans)


if __name__ == '__main__':
    s = Solution()
    nums = [8,1,2,2,3]
    print(s.smallerNumbersThanCurrent(nums))