nums1 = [4,3,2,3,1]
nums2 = [2,2,5,2,3,6]

##optimize##
set1 = set(nums1)
set2 = set(nums2)

common = set1.intersection(set2)
count1 = 0
for i in nums1:
    if i in common:
        count1+=1
count2 = 0
for j in nums2:
    if j in common:
        count2+=1
print (count1, count2)

# ans = []
# set1 = set(nums1)
# set2 = set(nums2)
# count = 0
# for i in nums1:
#     if i in set2:
#         count+=1
# ans.append(count)
# count = 0
# for j in nums2:
#     if j in set1:
#         count+=1
# ans.append(count)
# print (ans)