class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        
        heights.append(0)

        stack = []
        res = 0

        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:

                top = stack.pop()

                if stack:
                    width = i-stack[-1]-1
                    res = max(res,heights[top]*width)
                else:
                    width = i
                    res = max(res,heights[top]*width)

              

            stack.append(i)
                

        return res
