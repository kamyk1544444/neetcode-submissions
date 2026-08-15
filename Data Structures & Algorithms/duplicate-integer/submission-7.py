class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        poj = set()

        for num in nums:
            if num in poj:
                return True
            poj.add(num)
        return False