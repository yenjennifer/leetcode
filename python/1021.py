s = "(()())(())(()(()))"
# stack = []
# temp = [-1]
# ans = ""
# for i in range (len(s)):
#     if s[i] == ")":
#         if stack and stack[-1] == "(":
#             stack.pop()
#             if not stack:
#                 temp.append(i)
#     else:
#         stack.append(s[i])

# for i in range(len(temp)-1):
#     ans+=s[temp[i]+2:temp[i+1]]
# print(ans)

#open parentheses count == close parenteses count
result = ""
open_count = 0
for char in s:
    if char == '(':
        if open_count > 0:
            result += char
        open_count += 1
    else:
        open_count -= 1
        if open_count > 0:
            result += char
print(result) 