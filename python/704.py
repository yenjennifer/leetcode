nums = [-1,0,3,5,9,12]
target = 2

l = 0
r = len(nums)-1

while l<=r:
    m = (r+l)//2
    if target < nums[m]:
        r = m-1
    elif target > nums[m]:
        l = m+1
    else:
        print(m)

print(-1)