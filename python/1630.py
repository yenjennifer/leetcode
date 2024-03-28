nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]

ans = []
for i in range(len(r)):
    sub = sorted(nums[l[i]:r[i]+1])
    x = sub[1]-sub[0]
    for i in range(1,len(sub)):
        if sub[i]-sub[i-1] != x:
            ans.append(False)
            break
        elif i == len(sub)-1:
            ans.append(True)
print(ans)
