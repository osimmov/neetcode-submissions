class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seens, seent = {}, {}
        
        for i in range(len(s)):
            seens[s[i]] = 1 + seens.get(s[i], 0)
            seent[t[i]] = 1 + seent.get(t[i], 0)

        return seens == seent


        