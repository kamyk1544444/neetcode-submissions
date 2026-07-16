# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        wynik = []

        stak = collections.deque()
        stak.append(root)

        while stak:
            lista = []

            for i in range(len(stak)):
                node = stak.popleft()

                if node:
                    stak.append(node.left)
                    stak.append(node.right)
                    lista.append(node.val)
            if lista:
                wynik.append(lista)
        return wynik