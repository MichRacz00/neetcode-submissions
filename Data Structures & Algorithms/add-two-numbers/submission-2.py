# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0, None)
        curr = res

        while l1 or l2:
            val = 0
            if l1:
                val += l1.val
            if l2:
                val += l2.val
            
            if val // 10 > 0:
                if not l1.next:
                    l1.next = ListNode(0, None)
                l1.next.val += val // 10
                val = val % 10
            
            print(val)
            
            curr.next = ListNode(val, None)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return res.next