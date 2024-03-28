class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

        # if len(set(sentence)) < 26:
        #     return False
        # else:
        #     return True