# For example :
# Stack = [3,2,1,2,1,2]
# => Minstack = [3,2,1,1,1,1]

class MinStack:

    def __init__(self):
        self.MinStack = []
        self.stack = []

    def push(self, val: int) -> None:
        if self.MinStack: #not emtpy
            self.MinStack.append(min(val,self.MinStack[-1]))
        else:
            self.MinStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.MinStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()