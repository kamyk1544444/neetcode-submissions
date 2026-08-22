class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        stack = defaultdict(list)

        for a,b in prerequisites:
            stack[a].append(b)

        can = [0]*numCourses    
        res = []

        def func(num)->bool:

            if can[num] == 1:
                return False

            if can[num] == 2:
                return True

            can[num] = 1
                
            for val in stack[num]:
                if not func(val):
                    return False
            
            can[num] = 2
            res.append(num)
            return True
            
        for i in range(numCourses):
            if can[i] == 0:
                if not func(i):
                    return []
        

        return res