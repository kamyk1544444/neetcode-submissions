class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left, right = 0,n-1
        leftmax, rightmax = height[left],height[right]
        wynik = 0
        while left < right:

            if leftmax > rightmax:
                right -=1
                rightmax = max(rightmax,height[right])
                wynik += rightmax - height[right]
            else:
                left +=1
                leftmax = max(leftmax,height[left])
                wynik += leftmax - height[left]

        return wynik
            
