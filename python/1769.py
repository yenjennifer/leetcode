boxes = "001011"
dict = {}
zeroes = []
ones = []
index = 0
ans = []
for i in boxes:
    if i == '1':
        ones.append(index)
    index+=1
for j in range(len(boxes)):
    sum = 0
    for x in ones: #2,4,5
        sum += abs(x-j)
    ans.append(sum)
print(ans)