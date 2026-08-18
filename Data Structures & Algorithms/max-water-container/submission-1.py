class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left,right = 0,len(heights)-1
        res = 0

        
        while right > left:

            res = max(res,min(heights[left],heights[right]) * (right-left))

            if heights[right] >= heights[left]:
                left +=1
            else:
                right -=1

        return res