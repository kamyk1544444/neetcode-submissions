# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        wart1,wart2 = 0,0

        suma1,suma2 = 0,0

        cur1,cur2 = l1,l2

        while True:

            if cur1 is None and cur2 is None:
                break

            if cur1:
                wart1 += cur1.val * (pow(10,suma1))
                cur1 = cur1.next
                suma1 +=1
                
            if cur2:
                wart2 += cur2.val * (pow(10,suma2))
                cur2 = cur2.next
                suma2 +=1
        
        calk = wart1 + wart2
        dummy = ListNode(0)
        cur = dummy

        while True:       
            
            nowy = ListNode(calk % 10)
            calk = calk // 10

            cur.next = nowy
            cur = cur.next
            if calk == 0:
                break
            


            

        return dummy.next

            