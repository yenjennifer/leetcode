nums = [4,5,6,7,0,1,2]
target = 0

class Solution:
    def search(self, nums, target) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]: #sorted half is l~m
                if nums[l]<=target<nums[m]:
                    r = m #stay in this half
                else:
                    l = m+1 #search other half
            else: # sorted half is  m~r
                if nums[m]<target<=nums[r]:
                    l = m #stay in this half
                else:
                    r = m-1 #search other half
        return -1