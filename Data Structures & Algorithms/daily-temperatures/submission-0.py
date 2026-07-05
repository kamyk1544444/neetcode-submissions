class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        listy = [0] * n

        stack = []

        for i,temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
               st, si = stack.pop()
               listy[si] = i - si
            stack.append((temp,i))
        return listy