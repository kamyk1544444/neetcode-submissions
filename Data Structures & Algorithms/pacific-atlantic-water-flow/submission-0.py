class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights or not heights[0]:
            return []
        
        row,col = len(heights),len(heights[0])

        res = []

        atlantic = set()
        pacific = set()

        def dfs(r: int, c:int,visited, prev:int):
            if (not (0<=r<row) or not(0<=c<col) or (r,c) in visited or heights[r][c]<prev):
                return

            visited.add((r,c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])


        for c in range(col):
            dfs(0, c, pacific, heights[0][c])           
            dfs(row - 1, c, atlantic, heights[row - 1][c])  

        for r in range(row):
            dfs(r, 0, pacific, heights[r][0])           
            dfs(r, col - 1, atlantic, heights[r][col - 1])  

        for i in range(row):
            for j in range(col):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append((i,j))
        return res


