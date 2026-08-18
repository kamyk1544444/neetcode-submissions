class Solution:
    def isValid(self, s: str) -> bool:
        
        res = []

        charac = {
            "[":"]",
            "(":')',
            "{":"}"
        }

        for i in range(len(s)):

            if s[i] in charac:
                res.append(s[i])
                continue
            
            if not res or charac[res.pop()] != s[i]:
                return False

        
        return False if res else True