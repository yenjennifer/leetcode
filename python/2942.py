words = ["leet","code"]
x = "e"
# word = ""
# index = 0
# count = 0
# ans = []
# for i in words:
#     word = i
#     for j in word:
#         if j == x:
#             ans.append(index)
#             break
#     index +=1
# print (ans) 


############enumerate############
# Syntax: enumerate(iterable, start=0)
# Parameters:
# Iterable: any object that supports iteration
# Start: the index value from which the counter is to be started, by default it is 0
# Return: Returns an iterator with index and element pairs from the original iterable
print(list(enumerate(words))) #[(0, 'leet'), (1, 'code')]
ans=[]
for i,w in enumerate(words): 
    if x in w:
        ans.append(i)
print (ans) 
