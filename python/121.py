prices = [7,1,5,3,6,4]
l, r = 0,1
max_profit = 0
while r <= len(prices)-1:
    if prices[r]>prices[l]:
        max_profit = max(max_profit, prices[r]-prices[l])
    else:
        l = r
    r+=1
print(max_profit)