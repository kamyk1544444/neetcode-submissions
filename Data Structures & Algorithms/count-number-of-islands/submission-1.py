class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row,col = len(grid),len(grid[0])

        destination = [[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(i:int, j:int):
            
            q = deque()
            grid[i][j] = "0"
            q.append((i,j))
            while q:
                c,d =  q.popleft()
                
                for a,b in destination:
                    nc,nd = c+a,d+b
                    if (nc<0 or nc>=row or nd<0 or nd>=col or grid[nc][nd] == "0"):
                        continue
                    q.append((nc,nd))
                    grid[nc][nd] = "0"

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
