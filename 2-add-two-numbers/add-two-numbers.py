# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        p=0
        while l1 or l2:
            if l1:
                tmp1 = l1.val
                n1 += tmp1*10**p
                l1 = l1.next
            if l2:
                tmp2 = l2.val
                n2 += tmp2*10**p
                l2 = l2.next    
            p += 1
        sm = n1+n2
        l = [int(s) for s in str(sm)[::-1]]
        d=ListNode(0)
        c = d
        for t in l:
            c.next = ListNode(t)
            c = c.next
        return d.next




