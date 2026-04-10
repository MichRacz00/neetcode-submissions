# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode();
        ordered = dummy

        while lists:
            smallest = 0;
            head = lists[0]

            for i in range(len(lists)):
                if lists[smallest].val > lists[i].val:
                    smallest = i
            
            smallest_head = lists.pop(smallest)
            temp = smallest_head.next
            if temp:
                lists.append(temp)

            smallest_head.next = None
            ordered.next = smallest_head
            ordered = ordered.next

        return dummy.next