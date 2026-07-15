# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.same(root,subRoot):
            return True
        return (self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot))

    def same(self,root: Optional[TreeNode], subrot: Optional[TreeNode]) -> bool:
        
        if not root and not subrot:
            return True
        
        if root and subrot and root.val == subrot.val:
            return (self.same(root.left,subrot.left) and self.same(root.right,subrot.right))
        return False
