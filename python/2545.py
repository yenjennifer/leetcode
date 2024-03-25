score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2
klist = []
ans = []
for i in range(len(score)):
    klist.append((score[i][k],i))
    print(klist)
rank = sorted(klist, reverse = True)
for j in range(len(score)):
    ans.append(score[rank[j][1]])
print(ans)