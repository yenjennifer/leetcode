words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "bab"


def get_mapping(s):
    mapping = {}
    mapped_str = []
    idx = 0
    for char in s:
        if char not in mapping:
            idx += 1
            mapping[char] = idx
        mapped_str.append(mapping[char])
    return mapped_str

pattern_map = get_mapping(pattern)
ans = []
for word in words:    
    if pattern_map == get_mapping(word):
        ans.append(word)

print(ans)