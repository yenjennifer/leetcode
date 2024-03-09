class Solution:
    def findWordsContaining(self, words, x):
        word = ""
        index = 0
        ans = []
        for i in words:
            word = i
            for j in word:
                if j == x:
                    ans.append(index)
                    break
            index +=1
        return ans

if __name__ == '__main__':
    s = Solution()
    words = ["leet","code"]
    x = "e"
    print(s.findWordsContaining(words, x))

############enumerate############
        # ans=[]
        # for i,w in enumerate(words): 
        #     if x in w:
        #         ans.append(i)
        # return (ans) 

# Syntax: enumerate(iterable, start=0)
# Parameters:
# Iterable: any object that supports iteration
# Start: the index value from which the counter is to be started, by default it is 0
# Return: Returns an iterator with index and element pairs from the original iterable
# print(list(enumerate(words))) #[(0, 'leet'), (1, 'code')]

