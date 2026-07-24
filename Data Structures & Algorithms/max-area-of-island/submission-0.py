class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        destinations = [[0,-1],[1,0],[-1,0],[0,1]]

        row, col, count = len(grid),len(grid[0]),0

        def dfs(i:int , j:int)-> int:

            if (i<0 or j<0 or i>=row or j>= col or grid[i][j] == 0):
                return 0
            
            
            grid[i][j] = 0

            
            return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
     

        for i in range(row):
            for j in range(col):
                print("nowe")
                if grid[i][j] == 1:
                    count = max(count,dfs(i,j))

        return count
                    
