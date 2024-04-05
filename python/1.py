nums = [3,2,4]
target = 6
#O(1), O(1)
seen = {}
for i, num in enumerate(nums):
    print(i, num)
    complement = target - num
    if complement in seen:
        print([seen[complement], i])
    seen[num] = i

# O(N), O(N)
# from collections import Counter
# seen = set()
# for i in range(len(nums)):
#     if nums[i] in seen and 2*nums[i] == target:
#         print([i, nums.index(nums[i])])
#         break   
#     elif target - nums[i] in seen:
#         print([i, nums.index(target - nums[i])])
#         break
#     else:
#         seen.add(nums[i])