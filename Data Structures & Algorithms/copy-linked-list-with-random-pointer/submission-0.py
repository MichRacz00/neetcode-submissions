"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        all_copies = []
        rand_nodes = {}

        head_copy = head

        while head:
            copy = Node(head.val, None, None)
            if all_copies:
                all_copies[-1].next = copy
            all_copies.append(copy)
            rand_nodes[head] = copy
            head = head.next

        copy = all_copies[0]
        while head_copy:
            copy.random = rand_nodes.get(head_copy.random)
            head_copy = head_copy.next
            copy = copy.next
        
        return all_copies[0]
        