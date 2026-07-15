# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        root = self.odwroc(root)

        return root

    def odwroc(self,root) -> Optional[TreeNode]:
        
        if root is None:
            return None

        self.odwroc(root.right)
        self.odwroc(root.left)

        temp1 = root.right
        temp2 = root.left

        root.right = temp2
        root.left = temp1 

        return root

        

        