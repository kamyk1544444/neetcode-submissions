# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = list1
        curr2 = list2

        head = ListNode()
        res = head
        while curr1 is not None or curr2 is not None:

            if curr1 is not None and curr2 is not None:
                if curr1.val <= curr2.val:
                    res.next = curr1
                    curr1 = curr1.next
                else:
                    res.next = curr2
                    curr2 = curr2.next
            elif curr1 is not None:
                res.next = curr1
                curr1 = curr1.next
            elif curr2 is not None:
                res.next = curr2
                curr2 = curr2.next

            res = res.next

        return head.next