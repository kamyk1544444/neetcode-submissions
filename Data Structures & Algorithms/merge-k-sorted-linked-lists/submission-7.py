# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)<1:
            return None
        
        while len(lists)>1:
            merged = []
            
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(self.merg(l1,l2))
                
            lists = merged

        return lists[0]


    def merg(self, l1:ListNode,l2:ListNode)->ListNode:

        dummy = ListNode(0)
        curr = dummy
        curr1=l1
        curr2=l2


        while curr1 or curr2:

            val1 = curr1.val if curr1 else float("inf")
            val2 = curr2.val if curr2 else float("inf")

            if val1 == float("inf"):
                curr.next = curr2
                break
            elif val2 == float("inf"):
                curr.next = curr1
                break

            if val1 > val2:
                curr.next = curr2
                curr2 = curr2.next
            else:
                curr.next = curr1
                curr1 = curr1.next

            curr = curr.next
        
        return dummy.next



