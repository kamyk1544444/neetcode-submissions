# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedList

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    
        lista = SortedList()

        stack = deque([root])

        while stack:

            for i in range(len(stack)):
                node = stack.popleft()

                if node:
                    stack.append(node.right)
                    stack.append(node.left)   
                    lista.add(node.val)
                
        return lista[k-1]