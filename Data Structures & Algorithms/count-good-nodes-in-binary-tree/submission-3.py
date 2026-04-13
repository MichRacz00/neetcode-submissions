# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        def traverseTree(node: TreeNode, cur_max: int):
            if not node:
                return

            nonlocal good_nodes
            
            if node.val >= cur_max:
                good_nodes += 1
            
            cur_max = max(node.val, cur_max)
            
            traverseTree(node.left, cur_max)
            traverseTree(node.right, cur_max)

        traverseTree(root, root.val)

        return good_nodes