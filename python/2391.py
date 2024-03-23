garbage = ["G","G"]
travel = [1]
G = P = M = 0
n = len(garbage)
for i in range(n-1,0,-1):
    if "G" in garbage[i]:
        G = i
        break
for i in range(n-1,0,-1):
    if "P" in garbage[i]:
        P = i
        break
for i in range(n-1,0,-1):
    if "M" in garbage[i]:
        M = i
        break

sum = 0
#calculate distance:
for i in travel[0:G]:
    sum+=i
for i in travel[0:P]:
    sum+=i
for i in travel[0:M]:
    sum+=i
for i in garbage:
    sum+=len(i)
print(sum)