strs = ["eat","tea","tan","ate","nat","bat"]

from collections import defaultdict
map = defaultdict(list)
for word in strs:
    new_word = tuple(sorted(word))
    map[new_word].append(word)
print(map.values())

# seen = set()
# map = {}
# for word in strs:
#     new_word = tuple(sorted(word))
#     if new_word not in seen:
#         seen.add(new_word)
#         map[new_word] = [word]
#     else:
#         map[new_word].append(word)
# print(map.values())