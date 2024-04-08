numbers = [-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]
target = 4

class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1
        while r > l:
            while r > l and numbers[r] + numbers[l] > target:
                r-=1
            while r > l and numbers[r] + numbers[l] < target:
                l+=1
            if numbers[r] + numbers[l] == target:
                return [l+1,r+1]
        return []