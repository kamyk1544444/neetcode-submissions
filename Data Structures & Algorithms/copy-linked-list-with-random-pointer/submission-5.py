"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        old_to = defaultdict(lambda: Node(0))

        old_to[None] = None

        curr = head

        while curr:

            old_to[curr].val = curr.val

            old_to[curr].next = old_to[curr.next]
            old_to[curr].random = old_to[curr.random]

            curr = curr.next
        return old_to[head]
