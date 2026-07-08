class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       
        n=len(piles)

        l,r = 1,max(piles)
        wynik = r
        while r>= l:

            mid = l+ (r-l) // 2
            suma = 0

            for i in piles:
                suma += math.ceil(float(i) / mid)
            if suma <= h:
                wynik = mid
                r = mid-1
            else:
                l = mid+1
                
            
        
        return wynik
