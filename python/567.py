from collections import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1map, s2map = {}, {}
        for alphabet in string.ascii_lowercase:
            s1map[alphabet] = 0
            s2map[alphabet] = 0
        for i in range(len(s1)):
            s1map[s1[i]]+=1
            s2map[s2[i]]+=1
        
        hitCount = 0
        for alphabet in string.ascii_lowercase:
            if s1map[alphabet] == s2map[alphabet]:
                hitCount+=1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if hitCount == 26: return True

            s2map[s2[r]]+=1
            if s2map[s2[r]] == s1map[s2[r]]:
                hitCount+=1
            elif s2map[s2[r]] == s1map[s2[r]]+1:
                hitCount-=1
            
            s2map[s2[l]]-=1
            if s2map[s2[l]] == s1map[s2[l]]:
                hitCount+=1
            elif s2map[s2[l]] == s1map[s2[l]]-1:
                hitCount-=1
            l+=1
        return hitCount == 26
