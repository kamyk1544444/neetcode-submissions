class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)


        

        return [klucz for klucz,wartosc in count.most_common(k)]