class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        sizer = []

        for i in strs:
            sizer.append(str(len(i)))
            sizer.append(",")
        sizer.append("#")
        sizer.extend(strs)

        return "".join(sizer)
        
        
        
        
    def decode(self, s: str) -> List[str]:
       if not s:
        return []

       sizer,tabela, i = [],[],0

       while s[i] != "#":
        j=i;
        while s[j] != ",":
            j += 1
        sizer.append(int(s[i:j]))
        i=j+1

       i=i+1;

       for zakres in sizer:
        tabela.append(s[i:i+zakres])
        i += zakres;
       return tabela 
        
