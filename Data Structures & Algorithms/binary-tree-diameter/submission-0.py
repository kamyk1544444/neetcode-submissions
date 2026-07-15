# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        a,b = self.zlicz(root)
         
        return a

    def zlicz(self, root) -> tuple[int,int]:

        if root is None:
            return 0,0
        
        lewy_wart,lewy_wysok = self.zlicz(root.left)   

        prawy_wart,prawy_wysok = self.zlicz(root.right)

        szerekosc = max(lewy_wysok+prawy_wysok,lewy_wart,prawy_wart)

        obecny = 1 + max(lewy_wysok,prawy_wysok)

        return (szerekosc,obecny)


