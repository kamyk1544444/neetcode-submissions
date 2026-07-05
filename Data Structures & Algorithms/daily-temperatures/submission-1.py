class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        
        lista = [0]*n

        stack = []

        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                st,si = stack.pop()
                lista[si] = i-si
            stack.append((temp,i))
        return lista