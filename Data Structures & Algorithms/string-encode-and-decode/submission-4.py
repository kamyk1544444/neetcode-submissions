class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = []

        for slowo in strs:
            res.append(str(len(slowo)) + "*" + slowo)
        
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []

        start = 1
        i=0

        while i < len(s)-1:
            
            i +=1
            if s[i] != "*":
                start +=1
                continue
            
            lenght = int(s[i-start:i])
            res.append(s[i+1:i+lenght+1])
            i = i+lenght
            start = 0
            
            
        return res