class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        lengi = len(board)
        lengj = len(board[0])

        def dfs(index: int, i:int, j:int) ->bool:
        
            if i<0 or j<0 or i>=lengi or j>=lengj or index>len(word) or word[index] != board[i][j]:
                return False

            if index+1 == len(word) and word[index] == board[i][j]:
                return True 

            temp = board[i][j] 
            board[i][j] = "#"

            found = (
                dfs(index+1,i-1,j) or 
                dfs(index+1,i,j-1) or
                dfs(index+1,i+1,j) or
                dfs(index+1,i,j+1)
            )

            if found:
                return True

            board[i][j] = temp

            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == word[0]:
                    if dfs(0,i,j):
                        return True

        return False