# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        groupprev = dummy


        while True:
            
            kt = self.kth(groupprev,k)

            if not kt:
                break

            groupnext = kt.next

            prev,curr = kt.next, groupprev.next

            while curr !=groupnext:

                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupprev.next
            groupprev.next = kt
            groupprev = tmp




        return dummy.next



    def kth(self,curr,kt)->Optional[ListNode]:

        while curr and kt>0:
            kt -=1
            curr = curr.next
        
        return curr