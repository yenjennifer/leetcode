matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

class Solution:
    def searchMatrix(self, matrix, target):
        n = len(matrix[0])-1
        m = len(matrix)-1
        top, left = 0, 0
        bottom, right = m, n
        mid_row = (top+bottom)//2
        while bottom > top:
            if matrix[mid_row][n] > target:
                bottom = mid_row
            elif matrix[mid_row][n] < target:
                top = mid_row + 1
            else: 
                return True
            mid_row = (top+bottom)//2

        while left <= right:
            mid = (left+right)//2
            if matrix[mid_row][mid] > target:
                right = mid - 1
            elif matrix[mid_row][mid] < target:
                left = mid + 1
            else:
                return True
        return False