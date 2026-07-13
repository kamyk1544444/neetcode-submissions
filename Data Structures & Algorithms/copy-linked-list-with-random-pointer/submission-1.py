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
        
        dummy = collections.defaultdict(lambda : Node(0))

        dummy[None] = None

        cur = head

        while cur:
            dummy[cur].val = cur.val
            dummy[cur].next = dummy[cur.next]
            dummy[cur].random = dummy[cur.random]
            cur = cur.next

        return dummy[head]







