class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row,col, countfresh, = len(grid),len(grid[0]), 0
        destinations = [[0,1],[1,0],[-1,0],[0,-1]]
        rottenstack = deque()
        time = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    countfresh +=1
                elif grid[i][j] == 2:
                    rottenstack.append((i,j))
        
        
        while countfresh > 0 and rottenstack:

            for i in range(len(rottenstack)):
                r,c = rottenstack.popleft()

                for a,b in destinations:
                    g,h = r+a,c+b

                    if (g in range(len(grid)) and h in range(len(grid[0])) and grid[g][h] == 1 ):
                        countfresh -=1
                        rottenstack.append((g,h))
                        grid[g][h] = 2
            time +=1
                    
            
        return time if countfresh == 0 else -1