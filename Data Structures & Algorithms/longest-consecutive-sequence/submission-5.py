class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        pojemnik = set(nums)
        res = 0

        for num in pojemnik:

            if (num-1) not in pojemnik:

                dlugosc = 1

                while (num+dlugosc) in pojemnik:
                    dlugosc +=1
                    
                res = max(res,dlugosc)

        return res
