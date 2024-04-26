n = 3

stack = []
ans = []
def backtrack(open, close):
    if open == close == n:
        ans.append(''.join(stack))
        return
    if open < n:
        stack.append('(')
        backtrack(open+1, close)
        stack.pop()
    if close < open:
        stack.append(')')
        backtrack(open, close+1)
        stack.pop()

backtrack(0,0)
print(ans)