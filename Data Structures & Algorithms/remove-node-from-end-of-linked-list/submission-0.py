# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cel,suma = head,0

        while cel:
            suma +=1
            cel = cel.next
        
        dummy = ListNode(0, head)
        cur = dummy

        for _ in range(suma-n):
            cur = cur.next
        cur.next = cur.next.next

        return dummy.next