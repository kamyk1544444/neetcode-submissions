# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        wynik , daj = self.znajdz(root)

        return daj

    def znajdz(self, root) -> tuple[int,int]:

        if root is None:
            return 0,0
        
        lewy_sam,lewy = self.znajdz(root.left)

        prawy_sam,prawy = self.znajdz(root.right)


        wysokosc = 1 + max(prawy_sam,lewy_sam)

        szerekosc = max(lewy_sam+prawy_sam ,lewy,prawy)

        return wysokosc,szerekosc

