class Solution:
    def maxWidthOfVerticalArea(self, points):
        index = 0
        x_list =[]
        distance = []
        for i in points:
            x_list.append(i[0])
        x_list.sort()
        n = len(x_list)

        for j in x_list[:n-1]:
            distance.append(abs(j - x_list[index+1]))
            index+=1

        return (max(distance))

if __name__ == '__main__':
    s = Solution()
    points = [[8,7],[9,9],[7,4],[9,7]]
    print(s.maxWidthOfVerticalArea(points))
