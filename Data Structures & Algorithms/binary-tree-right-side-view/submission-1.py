# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        wynik = []

        def dfs(root,dept):
            if root is None:
                return None

            if dept == len(wynik):
                wynik.append(root.val)

            dfs(root.right,dept+1)
            dfs(root.left, dept+1)
        dfs(root,0)
        return wynik