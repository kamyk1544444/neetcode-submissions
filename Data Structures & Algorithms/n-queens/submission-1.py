class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        
        wynik = []
        pol = [["."] *n for i in range(n)]

        def backtrack(row: int):

            if row==n:
                kop = ["".join(r) for r in pol]
                wynik.append(kop)
                return
            for col in range(n):

                if sprawdz(row,col):
                    pol[row][col] = "Q"
                    backtrack(row+1)
                    pol[row][col] = "."


        def sprawdz(i:int,j:int) -> bool:
            row = i-1
            while row>=0:
                if pol[row][j] == "Q":
                    return  False
                row -=1
            
            row,col = i-1,j-1

            while row>=0 and col>=0:
                if pol[row][col] == "Q":
                    return False
                row -=1
                col -=1
            
            row,col = i-1,j+1

            while row>=0 and col<n:
                if pol[row][col] == "Q":
                    return False
                row -=1
                col +=1

            return True
        backtrack(0)

        return wynik