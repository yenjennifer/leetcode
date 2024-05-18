s = "BABABB"
k = 1

freq = {}
left = 0
max_len = 0
for right in range(len(s)):
    freq[s[right]] = freq.get(s[right], 0) + 1
    cur_len = right - left +1

    if cur_len - max(freq.values()) <=k:
        max_len = max(cur_len, max_len)

    else:
        freq[s[left]]-=1
        left += 1

print(max_len)