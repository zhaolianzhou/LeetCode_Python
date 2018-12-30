# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def transTree(t1, t2):
            t1.val += t2.val
            if t1.left is not None and t2.left is not None:
                transTree(t1.left, t2.left)
            if t1.right is not None and t2.right is not None:
                transTree(t1.right, t2.right)
            if t1.left is None:
                t1.left = t2.left
            if t1.right is None:
                t1.right = t2.right

        if t1 is None:
            return t2
        if t2 is None:
            return t1
        transTree(t1, t2)
        return t1

