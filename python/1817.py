##answer array: how many people there with UAM 1,2,3,...k)
logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
ans = [0] * k
seen = set()
map = {}
for user, time in logs:
    if (user, time) in seen: 
        continue
    map[user]= map.get(user,0)+1
    seen.add((user,time))
for value in map.values():
    if value <=k:
        ans[value-1]+=1
print(ans)

# for log in logs:
#     map[log[0]] = map.get(log[0],[])
#     if log[1] not in map[log[0]]:
#         map[log[0]].append(log[1])
# for key in map.keys():
#     ans[map[key]-1] +=1
# print(ans)