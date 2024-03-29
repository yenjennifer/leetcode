A = [1,3,2,4]
B = [3,1,2,4]
## two dictionaries##
dict_record = {}
ans = []
n = len(A)
for i in range(n):
    count = 0
    dict_record[A[i]] = dict_record.get(A[i], 0) +1
    dict_record[B[i]] = dict_record.get(B[i], 0) +1
    for k in dict_record.values(): # count the 2s in values
        if k ==2:
            count+=1
    ans.append(count)
print(ans)


##two sets##
n = len(A)
ans = []
set_a, set_b = set(), set()
for i in range(n):
    set_a.add(A[i])
    set_b.add(B[i])
    common = set_a & set_b
    if common:
        ans.append(len(common))
    else:
        ans.append(0)
print(ans)
