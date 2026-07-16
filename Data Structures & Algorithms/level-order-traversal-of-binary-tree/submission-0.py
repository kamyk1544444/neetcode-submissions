# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        wynik = []

        def szukaj(root,gleb):
            if root is None:
                return None
            
            if len(wynik) == gleb:
                wynik.append([])
            
            wynik[gleb].append(root.val)

            szukaj(root.left,gleb+1)
            szukaj(root.right,gleb+1)
        
        szukaj(root,0)
        return wynik

