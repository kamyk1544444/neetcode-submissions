class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        row, col = len(grid),len(grid[0])
        stack = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    stack.append((i,j))
        

        time = 1
        destinations = [[1,0],[0,1],[-1,0],[0,-1]]

        while stack:
            leng = len(stack)

            for i in range(leng):
                
                a,b = stack.popleft()

                for c,d in destinations:

                    nc,nb = a+c,b+d
                    
                    if (nc in range(row) and nb in range(col) and grid[nc][nb] == 2147483647):
                        grid[nc][nb] = time
                        stack.append((nc,nb))

            time +=1

        