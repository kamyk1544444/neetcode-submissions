class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if root is None or root.val == p.val or root.val == q.val:
            return root
        
        lewy = self.lowestCommonAncestor(root.left, p, q)
        prawy = self.lowestCommonAncestor(root.right, p, q)

        if lewy and prawy:
            return root
            
        # Ta linijka poniżej musi mieć dokładnie 8 spacji wcięcia (tak jak "if" powyżej)
        return lewy if lewy else prawy