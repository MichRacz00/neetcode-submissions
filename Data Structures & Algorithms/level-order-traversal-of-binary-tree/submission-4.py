# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        left, right = self.levelOrder(root.left), self.levelOrder(root.right)

        res = [[root.val]]

        while left or right:
            newNodes = []
            if left:
                newNodes += left.pop(0)
            if right:
                newNodes += right.pop(0)
            res.append(newNodes)
        
        return res