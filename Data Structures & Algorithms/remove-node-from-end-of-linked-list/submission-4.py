# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 0
        curr = head
        
        while curr:
            count +=1
            curr = curr.next

        curr = head
        if count-n == 0:
            return head.next
        for i in range(count-1):
            if count-n == (i+1):
                curr.next = curr.next.next
                break
            curr = curr.next

        return head