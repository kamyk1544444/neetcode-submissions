# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)

        grprev = dummy

        while True:
            h = self.znajdz(grprev,k)

            if not h:
                break
            grnext = h.next
            prev,cur = h.next,grprev.next

            while cur != grnext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            temp = grprev.next
            grprev.next = h
            grprev = temp

            
        return dummy.next
        
    def znajdz(self,cur,k):
        while cur and k > 0:
            cur = cur.next
            k -=1
        return cur