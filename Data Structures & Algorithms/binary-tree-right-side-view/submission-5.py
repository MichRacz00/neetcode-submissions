# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        left, right = self.rightSideView(root.left), self.rightSideView(root.right)

        res = [root.val]

        while left or right:
            level = []
            print(left, right)
            if left and not right:
                level.append(left.pop(0))
            if right:
                level.append(right.pop(0))
                if left:
                    left.pop(0)
            res += level
        
        return res