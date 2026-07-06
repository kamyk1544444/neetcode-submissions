class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i , j = 0, n-1
        wynik =0
        while i<j:
            
            wynik = max(wynik,min(heights[j],heights[i]) * (j-i))

            if heights[i] > heights[j]:
                j -=1
            else:
                i +=1
            

        return wynik
        