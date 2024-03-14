class Solution:
    def firstPalindrome(self, words):
        str = ""
        for element in words:
            if element == element[::-1]:
                str = element
                break
        return str