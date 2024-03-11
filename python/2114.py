class Solution:
    def mostWordsFound(self, sentences):
        nums = []
        for sentence in sentences:
            nums.append(sentence.count(" "))
        return max(nums) + 1
        # return max(sentence.count(" ") for sentence in sentences)+1
        # for sentence in sentences:
        #     spaces = 0
        #     for x in sentence:
        #         if x == " ":
        #             spaces +=1
        #     nums.append(spaces)
        # return max(nums) + 1

if __name__ == '__main__':
    s = Solution()  
    sentences = ["v and av","v"]
    print(s.mostWordsFound(sentences))