# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        po = 1

        number1 = 0
        number2 = 0

        curr1 = l1
        curr2 = l2

        while curr1 or curr2:
            if curr1:
                number1 +=  curr1.val*po
                curr1 = curr1.next

            if curr2:
                number2 +=  curr2.val*po
                curr2 = curr2.next
            
            
            
            po *=10

        suma = number1 + number2
        
        if suma == 0:
            return ListNode(0)

        dummy = ListNode(0)

        curr = dummy

        while suma > 0:
        
            if suma >= 10:
                number = suma%10
                suma = (suma-number)//10
            else:
                
                curr.next = ListNode(suma)
                curr = curr.next 
                break
            
            

            curr.next = ListNode(number)
            curr = curr.next 


        

        return dummy.next