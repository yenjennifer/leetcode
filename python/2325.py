key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"

alphabets = "abcdefghijklmnopqrstuvwxyz"
ans = ""
dict1 = {' ':' '} # input black space as blank space
index = 0
for i in key:
    if i not in dict1:
        dict1[i] = alphabets[index] # input mapping alphabet to key
        index+=1
for j in message:
    ans += dict1[j]
print(ans)


# mapping key to index, then  mapping index to alphabet's index; 
# need to consoder black space
# alphabets = "abcdefghijklmnopqrstuvwxyz"
# ans = ""
# dict1 = {}
# index = 0
# for i in key:
#     if i not in dict1 and i !=" ":
#         dict1[i] = index
#         index+=1

# for j in message:
#     if j != " ":
#         ans += alphabets[dict1[j]]
#     else:
#         ans+=" "
# print(ans)