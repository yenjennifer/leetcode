target = 10
position = [0,4,2]
speed = [2,1,3]

cars = [(p,s) for p,s in zip(position, speed)]
cars.sort(reverse=True)
count = 0
stack = []
for p,s in cars:
    time = (target - p)/s
    while stack and time > stack[-1]:
        stack.pop()
    if not stack:
        count+=1
    stack.append(time)
print(count) 

# pairs = [(p,s) for p,s in zip(position, speed)]
# pairs.sort(reverse=True)
# cur = res = 0
# for (p,s) in pairs:
#     time = (target - p)/s
#     if time > cur:
#         res+=1
#         cur = time
# print(res)