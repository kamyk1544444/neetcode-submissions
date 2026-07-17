# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedList

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    
        lista = SortedList()

        def dfs(root):
            if root is None:
                return None
            lista.add(root.val)

            dfs(root.right)
            dfs(root.left)
        
        dfs(root)
        
        return lista[k-1]