# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None

        i , curr = 0,lists[0]

        lista = []
        
        
        for curr in lists:
            while curr:
                heapq.heappush(lista,curr.val)
                curr = curr.next

        dummy = ListNode(0)
        curr = dummy

        while lista:
            naj = heapq.heappop(lista)
            nowy = ListNode(naj)
            curr.next = nowy
            curr = curr.next


        return dummy.next