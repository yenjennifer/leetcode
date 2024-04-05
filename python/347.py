nums = [4,1,-1,2,-1,2,3]
k = 2
from collections import Counter
map = Counter(nums)
list1 = []
ans = []
for i,j in map.items():
    list1.append((j,i))
list1 = sorted(list1, reverse = True)


for t in list1:
    if k!=0:
        ans.append(t[1])
        k-=1
print (ans)