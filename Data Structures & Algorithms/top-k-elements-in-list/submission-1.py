class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        licznik = Counter(nums)

        znajdz = licznik.most_common(k)

        return [element[0] for element in znajdz]