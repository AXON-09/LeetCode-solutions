# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode(0)
        cur = d
        c = 0
        while l1 or l2:
            if l1:
                tmp1 = l1.val
                l1 = l1.next
            else:
                tmp1 = 0
            if l2:
                tmp2 = l2.val
                l2 = l2.next 
            else:
                tmp2 = 0   
            n = tmp1 + tmp2 + c
            c = n // 10
            n = n % 10
            cur.next = ListNode(n)
            cur = cur.next
        if c:
           cur.next = ListNode(c)
        return d.next




