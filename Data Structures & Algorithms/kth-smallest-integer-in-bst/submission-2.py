# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversed = 0
        
        def inOrderTrav(root: Optional[TreeNode]) -> int:
            if not root:
                return -1

            nonlocal traversed
            res = inOrderTrav(root.left)
            if res > 0:
                return res
            traversed += 1
            if traversed == k:
                return root.val
            return inOrderTrav(root.right)
        
        return inOrderTrav(root)