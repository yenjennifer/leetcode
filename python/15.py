nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
# [-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]

def twoSum(numbers, target):
    l = 0
    r = len(numbers)-1
    list = []
    while r > l:
        if numbers[r] + numbers[l] == target:
            list.append([numbers[l], numbers[r], -target])
        if numbers[r] + numbers[l] > target:
            r-=1
        else:
            l+=1
    return list


nums_sort  = sorted(nums) 

seen = set()
for i in nums_sort:
    temp_list = nums_sort.copy()
    temp_list.remove(i)
    if twoSum(temp_list, -i)!= []:
        temp = twoSum(temp_list, -i)
        print(temp)
        for sub in temp:
            sub.sort()      
            seen.add(tuple(sub))

ans = []
for item in seen:
    ans.append(list(item))
print(ans)

print(len(ans))