# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        root_value = root.val

        def transTree(root, compare_value):
            if root.val != compare_value:
                return False
            elif root.left is not None and root.right is not None:
                return transTree(root.left, compare_value) and transTree(root.right, compare_value)
            elif root.left is not None:
                return transTree(root.left, compare_value)
            elif root.right is not None:
                return transTree(root.right, compare_value)
            else:
                return True

        return transTree(root, root_value)



