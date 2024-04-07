import string
s = "A man, a plan, a canal: Panama"
new = ""
for word in s:
    if word not in string.punctuation and word != " ":
        new  += "".join(word)
new.lower()

print(new)

if new == new[::-1]:
    print (True)
else:
    print(False)
