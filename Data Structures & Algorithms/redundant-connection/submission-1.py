class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        stack = [[] for _ in range(len(edges)+1)]


        def dfs(node,par):

            if visited[node]:
                return True

            visited[node] = True

            for nei in stack[node]:
                if nei == par:
                    continue
                if dfs(nei,node):
                    return True
            return False


        for a,b in edges:
            stack[a].append(b)
            stack[b].append(a)
            visited = [False] * (len(edges)+1)

            if dfs(a,-1):
                return [a,b]
        return []


