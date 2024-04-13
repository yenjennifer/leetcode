def minRectanglesToCoverPoints(points, w):
    
    points.sort()
    count = 1
    x = points[0][0]+ w
    for point in points:
        if point[0] <= x:
            continue
        else:
            x = point[0]+ w
            count+=1
    return count

points = [[2,1], [2,1], [2,1]]
w = 0
print(minRectanglesToCoverPoints(points, w))