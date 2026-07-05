class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pary = [(p,s) for p,s in zip(position,speed)]
        pary.sort(reverse=True)
        stack = []

        for p,s in pary: 
            stack.append((target-p) /s)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)