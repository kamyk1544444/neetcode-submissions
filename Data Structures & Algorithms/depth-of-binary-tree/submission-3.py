# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        q = deque([root])
        dept = 0

        while q:

            l = len(q)

            for i in range(l):
                p = q.popleft()
                
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)

            dept +=1

        return dept