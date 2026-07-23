class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        stack = []
        part = []

        def pali(slowo: str) -> bool:
            return slowo == slowo[::-1]

        def dfs(start):

            if start == len(s):
                stack.append(part.copy())
                return
            
            for end in range(start+1,len(s)+1):
                
                if pali(s[start:end]):
                    part.append(s[start:end])
                    dfs(end)
                    part.pop()
        dfs(0)

        return stack


                
            

        
        dfs(0)

        return stack
    
        

        