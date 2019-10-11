#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left is not None and root.left.val > root.val:
            return root.left.val
        if root.right is not None and root.right.val > root.val:
            return root.right.val

        return -1