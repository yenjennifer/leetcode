logs = ["d1/","d2/","../","d21/","./"]

#stack,TS O(N), O(N)
stack = []
for log in logs:
    if not stack and log == "../": #no more parent 
        continue
    elif log == "./":
        continue
    elif log == "../":
        stack.pop()
    else:
        stack.append(log)
print(len(stack))

#TS O(N), O(1])
class Solution:
    def minOperations(self, logs):
        count = 0
        for log in logs:
            if log == "../":
                if count > 0:
                    count -= 1
            elif log != "./":
                count += 1
        return max(0, count)
