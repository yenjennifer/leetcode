temperatures = [73,74,75,71,69,72,76,73]
#O(N)
n = len(temperatures)
ans = [0] * n
stack = []
for i in range(n):
    while stack and temperatures[i] > temperatures[stack[-1]]:
        top_idx = stack.pop()
        ans[top_idx] = i - top_idx
    stack.append(i)
print(ans)

#O(N^2)
# stack = []
# ans = []
# n = len(temperatures)
# for i in range(n-1):
#     stack.append(temperatures[i])
#     ptr = i+1
#     while ptr < n and stack:
#         if temperatures[ptr] > temperatures[i]:
#             ans.append(len(stack))
#             stack.clear()
#         else:
#             stack.append(temperatures[ptr])
#             if ptr == n-1:
#                 ans.append(0)
#                 stack.clear()
#             ptr+=1
# ans.append(0)
# print(ans)