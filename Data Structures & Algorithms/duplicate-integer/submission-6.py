class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        wynik = set()

        for i in nums:
            if i in wynik:
                return True
            wynik.add(i)
        return False