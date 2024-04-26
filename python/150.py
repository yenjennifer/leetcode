tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# operators = {'+', '-', '*', '/'}
stack = []
for token in tokens:
    if token in {'+', '-', '*', '/'}:
        x = stack.pop()
        y = stack.pop()
    if token == '+':
        stack.append(x+y)
    elif token == '-':
        stack.append(y-x)
    elif token == '*':
        stack.append(x*y)
    elif token == '/':
        stack.append(int(y/x))
    else:
        stack.append(int(token))
print(stack[0])