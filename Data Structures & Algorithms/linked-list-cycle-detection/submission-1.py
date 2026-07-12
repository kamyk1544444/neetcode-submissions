# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cos = head
        lista = defaultdict(int)
        while cos:
            if lista[cos]  > 0:
                return True
            lista[cos] +=1
            
            cos = cos.next
        return False