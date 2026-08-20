class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1,max(piles)

        res = right

        while left<=right:

            total = 0
            mid = left + (right-left) // 2

            for p in piles:
                total += math.ceil(p/mid)

            if total <= h:
                res = mid
                right = mid-1
            else:
                left = mid+1
        return res
