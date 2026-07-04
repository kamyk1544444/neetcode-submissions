class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        licznik = Counter(nums)

        wynik = licznik.most_common(k)

        wynikliczby = [element[0] for element in wynik]

        return wynikliczby