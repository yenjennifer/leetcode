from collections import Counter
nums = [1,3,4,1,2,3,1]
dic=Counter(nums)
key_list = list(dic.keys())
value_list = list(dic.values())
arr = [[0 for _ in range(0)] for _ in range(max(dic.values()))]

col_index = 0
for i in value_list:
    row_index = 0
    while i > 0:
        arr[row_index].append(key_list[col_index])
        i-=1
        row_index+=1
    col_index+=1
print(arr)

