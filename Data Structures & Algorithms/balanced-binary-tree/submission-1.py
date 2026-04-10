# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        if not root:
            return True
            
        def height(root: Optional[TreeNode]) -> int:
            nonlocal balanced
            if not root:
                return 0
            heightLeft, heightRight = height(root.left), height(root.right)
            if abs(heightLeft - heightRight) > 1:
                balanced = False
                print("not balanced", balanced)
            return max(heightLeft, heightRight) + 1

        height(root)

        return balanced
        
