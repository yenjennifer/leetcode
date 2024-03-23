bank = ["011001","000000","010100","001000"]
sum = 0
a = 0
for rows in bank:
    ones = rows.count("1")
    if ones: #if the count of 1s is not 0
        sum += ones*a
        a = ones
print(sum)