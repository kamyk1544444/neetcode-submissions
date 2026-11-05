class Solution:

    def encode(self, strs: List[str]) -> str:
        
        start = ""

        for st in strs:
            val = f"{len(st)}"

            start = "".join([start,val,"#",st])

        print(start)

        return start


    def decode(self, s: str) -> List[str]:

        
        res = []
        start = 0
        i=0
        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1
                continue
            print(start,i,len(s))
            val = int(s[i:j])
            res.append(s[j+1:j+1+val])
            i= j+1+val



        return res