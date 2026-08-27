class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(0)

        stack = []

        res = 0
        
        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:
                top = heights[stack.pop()]
                witdh = i if not stack else i-stack[-1]-1
                res = max(res,top*witdh)

            stack.append(i)
        
        return res