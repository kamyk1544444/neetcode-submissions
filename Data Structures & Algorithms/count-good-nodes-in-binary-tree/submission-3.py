# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 1

        a = self.szukaj(root.left,root.val)
        b = self.szukaj(root.right,root.val)
        c = 0
        print(a)
        print(b)
        
        print(a)
        return a+b+1

    def szukaj(self, root:TreeNode, maks) -> int:

        if root is None:
            return 0

        if root.val >= maks:
            return (self.szukaj(root.right,root.val)) + (self.szukaj(root.left,root.val)) + 1
        else:
            return (self.szukaj(root.right,maks)) + (self.szukaj(root.left,maks))
        
        
