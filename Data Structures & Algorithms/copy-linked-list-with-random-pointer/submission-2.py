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
        
        if head is None:
            return None
        
        cur = head

        while cur:
            stworz = Node(cur.val)
            kopia = cur.next
            cur.next = stworz
            stworz.next = kopia
            cur = stworz.next

        nowa = head.next

        cur = head

        while cur:
            if cur.random is not None:
                cur.next.random = cur.random.next 
            cur = cur.next.next
        cur = head

        while cur is not None:
            stworz = cur.next
            cur.next = stworz.next
            if stworz.next is not None:
                stworz.next = stworz.next.next
            cur = cur.next

        return nowa 
        







