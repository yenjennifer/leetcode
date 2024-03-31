arr = [2,3,1,6,7]
count = 0
for i in range(len(arr)-1):
    xor = arr[i]
    for j in range(i+1,len(arr)):
        xor ^= arr[j]
        if xor == 0:
            count += j-i
            ##from subarray i to j, count the possible rearrangements
print(count)
# (0,1,2), (0,2,2), (2,3,4), (2,4,4)