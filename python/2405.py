s = "ssssss"

##using set,TC:  O(N), O(N)
set1 = set()
count = 1
for i in range(len(s)):
    if s[i] not in set1:
        set1.add(s[i])
    else:
        count+=1
        set1.clear()
        set1.add(s[i])
print(count) 

##using strings, TC: O(N^2), O(N)
# temp = ""
# count = 1
# for i in s:
#     if i not in temp:
#         temp+=i
#     else:
#         temp = ""
#         temp+=i
#         count+=1
# print(count) 