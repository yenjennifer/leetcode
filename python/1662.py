class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        str1 = ""
        str2 = ""
        if str1.join(word1) == str2.join(word2):
            return True
        else:
            return False

        # for w1 in word1:
        #     str1 += w1
        # for w2 in word2:
        #     str2 += w2
        # if str1 == str2:
        #     return True
        # else:
        #     return False

if __name__ == '__main__':
    s = Solution()
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    print(s.arrayStringsAreEqual(word1, word2))
