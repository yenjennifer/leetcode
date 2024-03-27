s = "BABABB"
k = 1

freq = {}
left = 0
max_len = 0
for right in range(len(s)):
    freq[s[right]] = freq.get(s[right], 0) + 1
    cur_len = right - left +1
    print("cur_len", cur_len, "freq", freq)
    if cur_len - max(freq.values()) <=k:
        max_len = max(cur_len, max_len)
        print("right+1")
    else:
        freq[s[left]]-=1
        left += 1
        print("left+1")
print(max_len)


# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         k1 = k
#         arr = []
#         n = len(s)
#         for i in range(n):
#             left = i
#             right = i
#             length = 0
#             k1 = k
#             while right+1<=n:   
#                 if s[left] == s[right]:
#                     right += 1
#                     length += 1
#                 elif s[left] != s[right] and k1>0:
#                     right +=1
#                     k1-=1
#                     length+=1
#                 else:
#                     break
#             arr.append(length)

#         return max(arr)