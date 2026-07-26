class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1:
            return False

        stack = [[] for _ in range(n)]


        for a,b in edges:
            stack[a].append(b)
            stack[b].append(a)

        
        visited = set()

        def dfs(node):

            visited.add(node)

            for nei in stack[node]:
                if nei not in visited:
                    dfs(nei)
                    
            

        dfs(0)

        return len(visited) == n


