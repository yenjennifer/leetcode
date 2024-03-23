boxes = "001011"
ones = []
ans = []
index = 0
for i in boxes:
    if i == '1':
        ones.append(index)
    index+=1
for j in range(len(boxes)):
    sum = 0
    for x in ones: 
        sum += abs(x-j)
    ans.append(sum)
print(ans)