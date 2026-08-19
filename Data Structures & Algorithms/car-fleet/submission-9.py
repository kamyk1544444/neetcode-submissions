class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        for i in range(len(position)):
            stack.append([position[i],(target-(position[i])) / speed[i]])
        
        stack.sort(reverse=True)

        fleets = 1
        
        for i in range(1,len(stack),1):
            
            
            if stack[i][1] > stack[i-1][1]:
                fleets +=1
            else:
                stack[i][1] = max(stack[i][1],stack[i-1][1])

        return fleets