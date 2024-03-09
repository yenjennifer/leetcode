class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        max1 = max(candies)
        for candy in candies:
            if candy+extraCandies >= max1:
                result.append(True)
            else:
                result.append(False)
        return result
    
if __name__ == '__main__':
    s = Solution()
    candies = [2,3,5,1,3]
    extraCandies = 3
    print(s.kidsWithCandies(candies, extraCandies))