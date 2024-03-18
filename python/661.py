class Solution:
    def imageSmoother(self, img):
        row_arr = [-1,0,1]
        col_arr = [-1,0,1]
        n = len(img) #row
        m = len(img[0]) #column
        # ans=[[0]*m]*n 
        # cannot use this, *n is a shallow copy, it will change all the same row or colums and reference each other,
        # the iteration will be as such:
        # [[137, 0, 0], [137, 0, 0], [137, 0, 0]]
        # [[137, 141, 0], [137, 141, 0], [137, 141, 0]]
        # [[137, 141, 137], [137, 141, 137], [137, 141, 137]]
        # [[141, 141, 137], [141, 141, 137], [141, 141, 137]]
        # [[141, 138, 137], [141, 138, 137], [141, 138, 137]]
        # [[141, 138, 141], [141, 138, 141], [141, 138, 141]]
        # [[137, 138, 141], [137, 138, 141], [137, 138, 141]]
        # [[137, 141, 141], [137, 141, 141], [137, 141, 141]]
        # [[137, 141, 137], [137, 141, 137], [137, 141, 137]]
        # [[137, 141, 137], [137, 141, 137], [137, 141, 137]]        
        ans = [[0] * m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                sum = 0
                count = 0
                for i in row_arr:
                    for j in col_arr:
                        if row+i<0 or row+i==n or col+j<0 or col+j==m:
                            continue
                        sum += img[row+i][col+j]
                        count += 1
                ans[row][col] = sum//count
        return ans

if __name__ in '__main__':
    s = Solution()
    img = [[100,200,100],[200,50,200],[100,200,100]]
    print(s.imageSmoother(img))