allowed = "fstqyienx"
words = ["n","eeitfns","eqqqsfs","i","feniqis","lhoa","yqyitei","sqtn","kug","z","neqqis"]
set1 = set(allowed)
count = len(words)
for word in words:
    for letter in word:
        if letter not in set1:
            count -=1
            break
print(count)


# set1 = set(allowed)
# count = 0
# for i in words:
#     if set(i).issubset(set1):  ## have to create set for each word in words
#         count+=1
# print(count)