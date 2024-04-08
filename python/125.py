# def isPalindrome(self, s: str) -> bool:
#         new = ""
#         for word in s:
#             if word.isalnum():
#                 new += "".join(word.lower())
#         return new == new[::-1]
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize pointers for the start and end of the string
        left, right = 0, len(s) - 1
        
        # Loop until the pointers meet
        while left < right:
            # Move the left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            
            # Move the right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters at the pointers (ignoring case)
            if left < right and s[left].lower() != s[right].lower():
                return False
            
            # Move the pointers inward
            left += 1
            right -= 1
        
        # If the loop completes without returning False, the string is a palindrome
        return True
