class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        wynik = []

        def dfs(left:int,right: int ,sub: str):
            
            if left == n and right == n:
                wynik.append(sub)
                return
            if left < n:
                dfs(left+1,right,sub+"(")

            if right<left:
                dfs(left,right+1,sub+")")


            

        dfs(0,0,"")

        return wynik