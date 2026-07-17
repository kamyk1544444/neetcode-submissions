class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        wynik = float("-inf")
        n,suma = len(nums),1
        nums.sort()
        for i in range(n):
    
            if i+1 < n and nums[i] == nums[i+1]:
                continue
            if i+1 < n and nums[i+1]-nums[i] == 1:
                suma +=1
            else:
                suma = 1
            wynik = max(wynik,suma)

        return wynik