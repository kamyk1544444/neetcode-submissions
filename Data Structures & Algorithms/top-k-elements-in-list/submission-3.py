class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cont = {}
        freq = [[] for x in range(len(nums)+1)]
        for num in nums:
            cont[num] = 1+cont.get(num,0)

        for val,times in cont.items():
            freq[times].append(val)

        
        ret = []

        for i in range(len(nums),0,-1):
            for num in freq[i]:
            
                ret.append(num)
                if len(ret) == k:
                    return ret
        

        return ret