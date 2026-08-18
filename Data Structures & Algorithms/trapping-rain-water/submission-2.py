class Solution:
    def trap(self, height: List[int]) -> int:
        

        left, right = 0, len(height)-1

        leftmax,rightmax = height[left],height[right]


        res = 0

        while right>left:

            if height[left]>height[right]:
                right -=1
                rightmax = max(rightmax,height[right])
                res += rightmax - height[right]
            else:
                left +=1
                leftmax = max(leftmax,height[left])
                res += leftmax - height[left]

        return res 