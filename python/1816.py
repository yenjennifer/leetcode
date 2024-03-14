class Solution:
    def truncateSentence(self, s, k):
        # list = []
        # str = " "
        # list = s.split(" ")
        str = " ".join(s.split(" ")[:k])
        return str

if __name__ == '__main__':
    s1 = Solution()
    s = "What is the solution to this problem"
    k = 4
    print(s1.truncateSentence(s, k))