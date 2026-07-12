# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, lista1: Optional[ListNode], lista2: Optional[ListNode]) -> Optional[ListNode]:
       
        wynik = ListNode()

        aktualny = wynik

        while lista1 is not None or lista2 is not None:

            n = lista1.val if lista1 is not None else float('inf')
            m = lista2.val if lista2 is not None else float('inf')

            if n>m:
                aktualny.next =lista2
                lista2 = lista2.next
            else:
                aktualny.next = lista1
                lista1 = lista1.next
            
            aktualny = aktualny.next
        
        return wynik.next