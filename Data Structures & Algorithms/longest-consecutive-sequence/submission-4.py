class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        stack = set(nums)
        maksim = 0
        for i in stack:
            if (i-1) not in nums:
                dlugosc = 1

                while (i+dlugosc) in stack:
                    dlugosc +=1
                maksim = max(maksim,dlugosc)

        return maksim