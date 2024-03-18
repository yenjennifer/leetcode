pref = [5,2,0,3,1]

result = []
result.append(pref[0])
for n in range(len(pref)-1):
    result.append(pref[n] ^ pref[n+1])
print(result)


# class Solution:
#     def findArray(self, pref: List[int]) -> List[int]:
#         result = []
#         result.append(pref[0])
#         n = 0
#         for j in pref[:-1]:
#             result.append(pref[n] ^ pref[n+1])
#             n+=1
#         return result