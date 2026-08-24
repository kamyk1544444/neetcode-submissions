# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 0

        dummy = ListNode()
        go = dummy
        curr = head
        
        while curr:
            count +=1
            curr = curr.next

        curr = head

        print(count-n)
        cnt = 0 
        while curr:
            print(count-n,cnt)
            if count-n != cnt:
                print("wchodze")
                go.next = curr
                go = go.next

            curr = curr.next
            cnt +=1
        if n==1:
            go.next = None
        return dummy.next