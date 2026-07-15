# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        zbalansowany, ile = self.sprawdz(root)
        
        return zbalansowany

    def sprawdz(self,root) -> tuple[bool,int]:

        if root is None:
            return True,0
        
        lewyy,lile = self.sprawdz(root.left)

        prawyy,pile = self.sprawdz(root.right)

        warunek = (lewyy and prawyy and abs(lile-pile) <= 1)

        ilosc = 1 + max(lile,pile)

        return warunek,ilosc
        


