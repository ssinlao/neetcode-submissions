# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # invert each level of the tree
        # level 0 will always be the same
        # to invert always start from right most

        if not root:
            return None

        # swapping nodes
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursive
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root