class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        lengi = len(board)
        lengj = len(board[0])

        def dfs(index: int, i:int, j:int, slowo:str) ->bool:
            if slowo == word:
                return True
            print(board[i][j],word[index])
            if board[i][j] != word[index]:
                return False
            temp = board[i][j] 
            board[i][j] = "#"
            if i>0:
                if dfs(index+1,i-1,j,slowo+board[i-1][j]):
                    return True
            if j>0:
                if dfs(index+1,i,j-1,slowo+board[i][j-1]):
                    return True
            if i+1<lengi:
                if dfs(index+1,i+1,j,slowo+board[i+1][j]):
                    return True
            if j+1<lengj:
                if dfs(index+1,i,j+1,slowo+board[i][j+1]):
                    return True
                    
            board[i][j] = temp

            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == word[0]:
                    if dfs(0,i,j,board[i][j]):
                        return True

        return False