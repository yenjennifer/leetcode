nums = [4,5,6,7,0,1,2]
l, r = 0, len(nums)-1
while l<=r:
    m = (l+r)//2
    if nums[m] > nums[r]:
        l = m+1
    elif nums[m] < nums[r]:
        r = m
    else:
        print(nums[m])
        break
print(nums[m])