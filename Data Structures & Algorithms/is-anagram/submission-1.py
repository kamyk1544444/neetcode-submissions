class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        scont = [0]*26
        tcont = [0]*26

        for i in range(len(s)):
            scont[ord(s[i]) - ord("a")] +=1
            tcont[ord(t[i]) - ord("a")] +=1
        
        for i in range(26):

            if scont[i] != tcont[i]:
                return False

        return True