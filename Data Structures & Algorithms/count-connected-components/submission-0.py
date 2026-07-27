class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        

        stack = [[] for _ in range(n)]

        visited = [False for _ in range(n)]

        for a,b in edges:
            stack[a].append(b)
            stack[b].append(a)

        
        count = 0
       
        def dfs(node):

            if visited[node]:
                return

            visited[node] = True

            for nei in stack[node]:
                if not visited[nei]:
                    dfs(nei)
                    
             


        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count +=1

        return count