nums = [1,2,2,2,1,3]
k = 1

count = 0
dict = {}
for i in nums:
    dict[i] = dict.get(i, 0) +1 ######dict=Counter(nums)

for key in dict:
    if key + k in dict:
        count += dict[key] * dict[key+k]
print(count)

# from collections import Counter 
# dic=Counter(nums)
# count=0
# for i in dic:
#     if i+k in dic:
#         count+=dic[i]*dic[i+k]