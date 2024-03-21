class Solution:
    def countPoints(self, points, queries):
        result = []
        for X, Y, R in queries:
            count = 0
            for x, y in points:
                if (x-X)**2+(y-Y)**2 <= R**2:
                    count+=1
            result.append(count)
        return result