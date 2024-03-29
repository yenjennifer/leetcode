s = "leetcode"
t = "practice"

# count = 0
# for i in set(t):
#     count += max(t.count(i) - s.count(i), 0)
# print(count)

from collections import Counter
dict_s = Counter(s)
dict_t = Counter(t)
count = 0
for i in list(dict_t.keys()): ## i is t key
    if i in dict_s.keys():
        count +=  max(dict_t[i] - dict_s[i],0)
        # if dict_t[i] <= dict_s[i]:
        #     continue
        # else:
        #     count +=  dict_t[i] - dict_s[i]
    else:
        count+=dict_t[i]
print(count)

# list1 = [0]*26
# for tt in t:
#     list1[ord(tt)-ord('a')]+=1
# for ss in s:
#     list1[ord(ss)-ord('a')]-=1
# count = 0
# for c in list1:
#     count += abs(c)
# print(count//2)