# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:

            lista = []
            
            for i in range(len(q)):
                c = q.popleft()

                if c:
                    lista.append(c.val)
                    q.append(c.left)
                    q.append(c.right)
            if lista:
                res.append(lista)

        return res
