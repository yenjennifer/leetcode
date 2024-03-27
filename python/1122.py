arr = [10,11,12]
n = len(arr)
ans = 0
# ans = sum(arr)
temp = sum(arr[0:1])
for length in range(3, n+1, 2):
    presum = temp + arr[length-2] + arr[length-1]
    temp = presum
    ans += presum
    for start in range (1,n-length+1):
        presum = presum - arr[start-1] + arr[start+length-1]
        ans+=presum

if n%2 !=0:
    ans+=temp
else:
    ans+= temp + arr[n-1]

print(ans)