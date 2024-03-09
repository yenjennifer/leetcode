class Solution:
    #create empty list in l = 2n
    #append input list to each other
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        for element in nums:
            ans.append(element)
        return ans

        #return nums+nums