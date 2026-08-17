class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = []

        for slowo in strs:
            res.append(str(len(slowo)) + "*" + slowo)
        
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        i=0

        while i < len(s):
            
            start = s.find('*',i)

            lenght = int(s[i:start])

            res.append(s[start+1:start+1+lenght])

            i = start+lenght+1
            
            
        return res