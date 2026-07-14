# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        zbalanswoany, ile = self.sprawdz(root)

        return zbalanswoany
        
    def sprawdz(self,root) -> tuple[bool,int]:

        if root is None:
            return True,0
        lewy_balans, wartosc = self.sprawdz(root.left)

        prawy_balans, wart = self.sprawdz(root.right)


        warunki = (
            lewy_balans and prawy_balans and abs(wartosc-wart) <= 1
        )

        obecny = 1 + max(wartosc,wart)

        return warunki,obecny


