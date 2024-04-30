import math
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        n = len(piles)
        #edge#
        if n == 1:
            res = math.ceil(piles[0]/h)
            return res
        else:
            min_k, max_k = 1, max(piles)
            while min_k <= max_k:
                hours = 0
                mid = (min_k+max_k)//2
                for p in piles:
                    hours += math.ceil(p/mid)
                if hours > h:
                    min_k = mid+1
                elif hours <= h:
                    res = mid
                    # save the result if sum of time is under threshold
                    max_k = mid-1 
                    # try to find a smaller amount of k for minimum eating spped
            return res

if __name__ == '__main__':
    s = Solution()
    piles = [30,11,23,4,20]
    h = 5
    print(s.minEatingSpeed(piles, h))
