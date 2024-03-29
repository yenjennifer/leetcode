# words = ["gin","zen","gig","msg"]
# morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# alphabets = "abcdefghijklmnopqrstuvwxyz"
# ans = []
# for word in words:
#     new = ""
#     for letter in word:
#         new+= morse[alphabets.index(letter)]
#     ans.append(new)
# print(len(set(ans)))


## optimize ##
words = ["gin","zen","gig","msg"]
morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
alphabets = "abcdefghijklmnopqrstuvwxyz"
morse_dict = dict(zip(alphabets, morse))
ans = []
for word in words:
    new = ""
    for letter in word:
        new+=morse_dict[letter]
    ans.append(new)
print(len(set(ans)))

