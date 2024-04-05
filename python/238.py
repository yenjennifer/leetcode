nums = [2,2,3,4]
n = len(nums)
ans = n*[0]


if nums.count(0) > 1:
    print(ans)
else:
    product = 1
    for i in range(n):
        ans[i] = product
        product *= nums[i]

    product = 1
    for i in range(n-1, -1, -1):
        ans[i] = product * ans[i]
        product *= nums[i]
    print(ans)


# map = {}
# x = nums.count(0)
# if x == 0:
#     Situation = 0
# elif x == 1:
#     Situation = 1
# else:
#     Situation = 2

# product = 1
# if Situation == 2:
#     print(len(nums)*[0])
# elif Situation == 1:
#     for i in nums:
#         if i!=0:
#             product*=i
#     for i in nums:
#         if i==0:
#             map[i] = product
#         else:
#             map[i] = 0

# elif Situation == 0:
#     for i in nums:
#         product*=i
#     map[1] = product
#     map[-1] = -product
#     for i in nums:
#         if i in map.keys():
#             continue
#         elif -i in map.keys():
#             map[i] = -map[-i]
#         else:
#             temp = product
#             val = 0
#             while temp!=0:
#                 if temp*i>0:
#                     temp-=i
#                 else:
#                     temp+=i
#                 val+=1
#             map[i] = val
# ans = []
# for i in nums:
#     ans.append(map[i])
# print(ans)