candies = [4,2,1,1,2]
extraCandies = 1
result = []
for candy in candies:
    new_candies = candy+extraCandies
    if new_candies > max(candies):
        result.append(True)
    else:
        result.append(False)
print (result)
print (type(result))