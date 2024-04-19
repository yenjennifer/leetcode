class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        set1 = set()
        for word in s[::-1]:
            if 1 in set1 and word==" ":
                break
            if word == " ":
                set1.add(0)
            else:
                set1.add(1)
                count+=1
        return count