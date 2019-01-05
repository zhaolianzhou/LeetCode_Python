# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val == val:
            return root

        def searchHelp(root, val):
            if root.val == val:
                return root
            if root.left is not None:
                result = searchHelp(root.left, val)
                if result is not None:
                    return result
            if root.right is not None:
                result = searchHelp(root.right,val)
                if result is not None:
                    return result
            return None

        return searchHelp(root, val)
