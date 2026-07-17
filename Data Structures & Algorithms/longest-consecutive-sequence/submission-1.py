class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        stack = []

        for i in nums:
            stack.append(i)

        wynik = float("-inf")
        n,suma = len(stack),1
        stack.sort()
        for i in range(n):
    
            if i+1 < n and stack[i] == stack[i+1]:
                continue
            if i+1 < n and stack[i+1]-stack[i] == 1:
                suma +=1
            else:
                suma = 1
            wynik = max(wynik,suma)

        return wynik