class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = ""

        for slowo in strs:
            res += str(len(slowo)) + "*" + slowo
        
        return res


    def decode(self, s: str) -> List[str]:
        res = []

        start = 1
        i=0
        print(s,len(s))
        while i < len(s)-1:
            
            i +=1
            if s[i] != "*":
                start +=1
                continue
            print("teraz lece jak najman ",i)
            print(s[i-start:i])
            print(i-start,start)
            lenght = int(s[i-start:i])
            res.append(s[i+1:i+lenght+1])
            print(lenght,"wartposc lengh")
            print(s[i+1:i+lenght+1])
            i = i+lenght
            print("po",i)
            start = 0
            
            
        return res