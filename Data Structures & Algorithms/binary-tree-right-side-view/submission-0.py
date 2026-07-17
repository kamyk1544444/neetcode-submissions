# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        wynik = []

        stack = deque([root])

        while stack:
            right = None
            One = None

            for i in range(len(stack)):
                node = stack.popleft()
                
                if node:
                    stack.append(node.right)
                    stack.append(node.left)
                    right = node

                if One is None and right:
                    One = right
                    wynik.append(right.val)
                    
        return wynik
        
