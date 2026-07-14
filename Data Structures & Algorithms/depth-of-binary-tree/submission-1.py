# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        wynik = 1

        if root.left is not None:
            wynik = max(wynik, self.wejdz(root.left,2))
        if root.right is not None:
            wynik = max(wynik, self.wejdz(root.right,2))

        return wynik
        
    def wejdz(self,root,k):

        maxk = k
        
        if root.left is not None:
            maxk = max(maxk,self.wejdz(root.left,k+1))


        if root.right is not None:
            maxk = max(maxk,self.wejdz(root.right,k+1))
     
        return maxk