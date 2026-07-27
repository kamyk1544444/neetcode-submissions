class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)

        stack = [[] for _ in range(n+1)]
        visit = [False for _ in range(n+1)]

        for a,b in edges:
            stack[a].append(b)
            stack[b].append(a)


        cycle = set()
        cyclestart = -1


        def dfs(node,par):
            nonlocal cyclestart

            if visit[node]:
                cyclestart = node
                return True
            
            visit[node] = True

            for nei in stack[node]:
                if nei == par:
                    continue

                if dfs(nei,node):

                    if cyclestart != -1:
                        cycle.add(node)
                    if node == cyclestart:
                        cyclestart = -1
                    return True
            return False 
  
  


        dfs(1,-1)

        for a,b in reversed(edges):
            if a in cycle and b in cycle:
                return [a, b]
        return []