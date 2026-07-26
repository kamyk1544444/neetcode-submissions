class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        stack = [[] for i in range(numCourses)]

        for a,b in prerequisites:
            stack[a].append(b)

        visited = set()
        cycle = set()
        out = []

        def dfs(crs):

            if crs in cycle:
                return False
            
            if crs in visited:
                return True
            
            cycle.add(crs)

            for i in stack[crs]:
                if not dfs(i):
                    return False


            cycle.remove(crs)
            visited.add(crs)
            out.append(crs)

            return True


        

        for i in range(numCourses):
            if not dfs(i):
                return []
        return out