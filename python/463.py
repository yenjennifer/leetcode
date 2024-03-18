grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
perimeter = 0
r = len(grid)
c = len(grid[0])
for i in range (r):
    for j in range (c):
        if grid[i][j] == 1:
            perimeter+=4
            if i > 0 and grid[i-1][j] == 1:
                perimeter-=2
            if j > 0 and grid[i][j-1] == 1:
                perimeter-=2
print(perimeter)

# Traverse the grid block by block
# If the block is land increment perimeter by 4 and check it's top and left neighbours.
# If the neighbours are land blocks decrement perimeter by 2 per intersection.
# Repeat the process until the whole grid is traversed