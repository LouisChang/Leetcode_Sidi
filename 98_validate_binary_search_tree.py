# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, -2147483648.1, 2147483647.1)

    def isValid(self, root, min, max):
        if not root:
            return True
        if root.val <= min or root.val >= max:
            return False

        return self.isValid(root.left, min, root.val) and self.isValid(root.right, root.val, max)
