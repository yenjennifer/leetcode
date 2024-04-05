class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        def is_anagram(string):
            map = {}
            for char in string:
                map[char] = map.get(char, 0)+1
            return map

        return(is_anagram(s)==is_anagram(t))