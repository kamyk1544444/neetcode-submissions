# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        wynik = self.sprawdz(p,q)

        return wynik

    def sprawdz(self,root: Optional[TreeNode],node: Optional[TreeNode]) -> bool:

        if root is None and node is None:
            return True
        if root is None or node is None:
            return False
     
        if root.val != node.val:
            return False
        

        one = self.sprawdz(root.right, node.right)
        two = self.sprawdz(root.left,node.left)
        if one is False or two is False:
            return False
        return True