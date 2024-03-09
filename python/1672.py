accounts = [[2,8,7],[7,1,3],[1,9,5]]
wealth = []
for i in accounts:
    sum1 = sum(i)
    wealth.append(sum1)
print (max(wealth))