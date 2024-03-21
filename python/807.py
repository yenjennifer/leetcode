grid = [[3,0,8,4],
        [2,4,5,7],
        [9,2,6,3],
        [0,3,1,0]]

n = len(grid)
sum = 0
row_max = []
col_max = []
for i in range(n):
    row_max.append(max(grid[i]))
    temp = 0
    for j in range(n):
        if grid[j][i] > temp:
            temp = grid[j][i]
    col_max.append(temp)
for i in range(n):
    for j in range(n):
        sum+=min(row_max[i], col_max[j])-grid[i][j]
print(sum)

# import numpy
# n = len(grid)
# grid_t = numpy.transpose(grid)
# sum= 0
# for i in range(n):
#     for j in range(n):
#         sum+=min(max(grid[i]),max(grid_t[j]))-grid[i][j]
# print(sum)