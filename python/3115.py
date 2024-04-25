nums = [3,17]
res = []
for i in range(len(nums)):
    num = nums[i]
    if num > 1:
        for k in range(2, (num//2)+1):

            if (num % k) == 0:
                break
        else:
            res.append(i)
print(res)
print(res[len(res)-1]- res[0])