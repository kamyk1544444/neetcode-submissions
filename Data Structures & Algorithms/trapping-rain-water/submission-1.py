class Solution:
    def trap(self, height: List[int]) -> int:
        

        l,r=0,len(height)-1
        leftmax, rightmax = height[l],height[r]
        wynik =0

        while r > l:

            if leftmax > rightmax: 
                r -=1
                rightmax = max(rightmax,height[r])
                wynik += rightmax - height[r]
            else:
                l +=1
                leftmax = max(leftmax,height[l])
                wynik += leftmax - height[l]

        return wynik
            
