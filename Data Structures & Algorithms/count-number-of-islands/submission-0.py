class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row,col = len(grid),len(grid[0])

        destination = [[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(i:int, j:int):
            

            if (i<0 or j<0 or i>= row or j>= col or grid[i][j] == "0"):
                return

            grid[i][j] = "0" 

            for a,b in destination:
                dfs(i+a,b+j)
                
        count = 0

        for i in range(row):
            for j in range(col):

                if grid[i][j] == "1":
                    dfs(i,j)
                    count +=1
        
        return count
