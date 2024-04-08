height = [1,8,6,2,5,4,8,3,7]
n = len(height)
l = 0
r = n-1
max_area = 0
while l < r:
    area = min(height[l], height[r])*(r-l)
    if height[l] < height[r]:
        l+=1
    else:
        r-=1
    max_area = max(area, max_area)
print(max_area)