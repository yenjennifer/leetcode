class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rectangle = rectangle
    
    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for x in range(row1, row2+1):
            for y in range(col1, col2+1):
                self.rectangle[x][y] = newValue
        return self.rectangle

    def getValue(self, row, col):
        return self.rectangle[row][col]


rectangle = [[1,2,1],[4,3,4],[3,2,1],[1,1,1]]
obj = SubrectangleQueries(rectangle)
x = obj.getValue(0, 2)
print(x)