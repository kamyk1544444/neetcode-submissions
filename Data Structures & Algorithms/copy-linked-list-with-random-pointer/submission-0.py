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
        
        dummy = {None : None}

        cur = head

        while cur:
            dummy[cur] = Node(cur.val)
            cur = cur.next
    
        cur = head

        while cur:
            kopia = dummy[cur]
            kopia.next = dummy[cur.next]
            kopia.random = dummy[cur.random]
            cur = cur.next
        return dummy[head]






